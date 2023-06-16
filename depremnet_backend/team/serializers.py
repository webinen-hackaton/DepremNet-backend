from rest_framework import serializers
from . models import Team, TeamType, Job, Status


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ["id"]

class TeamTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamType
        fields = '__all__'
        read_only_fields = ["id"]

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        read_only_fields = ["id"]

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'
        read_only_fields = ["id"]



# class TeamSerializer(serializers.Serializer): 
#     id = serializers.IntegerField(read_only=True)
#     team_name = serializers.CharField(max_length=50)
#     team_type = serializers.ForeignKey(TeamType, on_delete=models.DO_NOTHING)
#     location = fields.PointField(verbose="location")
#     team_status = serializers.ForeignKey(Status, on_delete=models.DO_NOTHING)

#     def create(self, validated_data):
#         return Team.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.