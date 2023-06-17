from rest_framework import (
    views, 
    response, 
    exceptions
)
from .serializers import (
    TeamSerializer,
    TeamTypeSerializer,
    StatusSerializer,
    JobSerializer
)
from .models import (
    Team,
    TeamType,
    Status,
    Job
)
from django.http import JsonResponse

from . import services, authentication
from rest_framework import permissions

class TeamApi(views.APIView):
    authentication_classes = (authentication.CustomAuthentication, )
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

    def get(self, request): # get all

        try:
            user = request.user
            teams = Team.objects.filter(team_manager=user)
            serializer = TeamSerializer(teams, many=True)
            data = serializer.data

            for item in data:
                team_type = TeamType.objects.get(pk=item['team_type'])
                team_status = Status.objects.get(pk=item['team_status'])
                team_type_serializer = TeamTypeSerializer(team_type)
                team_status_serializer = StatusSerializer(team_status)
                item['team_type'] = team_type_serializer.data
                item['team_status'] = team_status_serializer.data

            return response.Response(data)
        except Team.DoesNotExist:
            raise exceptions.NotFound("Teams not found")
        except Exception as e:
            return response.Response({"error": str(e)}, status=500)

    def post(self, request):# create one 
        if not request.user.is_staff:
            raise exceptions.AuthenticationFailed("Only admin user can create a team!")

        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        return response.Response(serializer.errors, status=400)
    
class TeamByIdApi(views.APIView):
    authentication_classes = (authentication.CustomAuthentication, )
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)
    
    def get(self, request, team_id): #get one by id
        try:
            team = Team.objects.get(pk=team_id)
            serializer = TeamSerializer(team)
            data = serializer.data
            
            team_type = TeamType.objects.get(pk=data['team_type'])
            team_status = Status.objects.get(pk=data['team_status'])
            team_type_serializer = TeamTypeSerializer(team_type)
            team_status_serializer = StatusSerializer(team_status)
            data['team_type'] = team_type_serializer.data
            data['team_status'] = team_status_serializer.data
            
            return response.Response(data)
        except Team.DoesNotExist:
            raise exceptions.NotFound("Team not found")
        except Exception as e:
            return response.Response({"error": str(e)}, status=500)
    
    def put(self, request, team_id): # update one by id
        try:
            team = Team.objects.get(pk=team_id)
            serializer = TeamSerializer(team, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data)
            return response.Response(serializer.errors, status=400)
        except Team.DoesNotExist:
            raise exceptions.NotFound("Team not found")
        except Exception as e:
            return response.Response({"error": str(e)}, status=500)

    def delete(self, request, team_id):# delete on by id
        try:
            team = Team.objects.get(pk=team_id)
            team.delete()
            return response.Response({"message":f"Team Id:{team_id} has been deleted!"},status=204)
        except Team.DoesNotExist:
            raise exceptions.NotFound("Team not found")
        except Exception as e:
            return response.Response({"error": str(e)}, status=500)


class TeamTypeApi(views.APIView):

    def get(self, request):
        types = TeamType.objects.all()
        serializer = TeamTypeSerializer(types, many=True)
        return response.Response(serializer.data)

class TeamStatusApi(views.APIView):
   
   def get(self, request):
        status = Status.objects.all()
        serializer = StatusSerializer(status, many=True)
        return response.Response(serializer.data)

class JobApi(views.APIView):
    
    def get(self, request): # list all jobs (mmedical, etc.)
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return response.Response(serializer.data)


class AddTeamMemberById(views.APIView):
    # authentication_classes = (authentication.CustomAuthentication, )
    # permission_classes = (permissions.IsAuthenticated, )

    def put(self, request, team_id, user_id):
        team, user = services.get_team_and_user(team_id, user_id)

        if not user.is_staff:
            raise ValueError("user should be a member for including to a team")

        if user.team_id is not None:
            raise ValueError("member should not be in another group")

        user.team_id = team.id
        user.save()

        return response.Response(data={"message": f"member added to team: {user.id} -> {team.id}"})

class RemoveTeamMemeberById(views.APIView):
    
    def put(self, request, team_id, user_id):
        team, user = services.get_team_and_user(team_id, user_id)

        if user.team_id is None:
            raise ValueError("User should ne in a team for removing request")
        
        user.team_id = None
        user.save()

        return response.Response(data={"message": f"user successfully removed from team: {user.id} -> {team.id}"})