from rest_framework import serializers
from api.models import Entry
class EntrySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Entry

        fields = ('url','pk','name','city','school','link','lat','lng','address','distance','time','contact',
                  'score','comments','sell','image','owner')

