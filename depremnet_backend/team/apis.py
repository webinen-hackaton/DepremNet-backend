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


class TeamApi(views.APIView):
    def get(self, request): # get all
        try:
            teams = Team.objects.all()
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
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=201)
        return response.Response(serializer.errors, status=400)
    
class TeamByIdApi(views.APIView):
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
