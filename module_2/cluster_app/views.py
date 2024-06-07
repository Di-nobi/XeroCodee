from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ClusterDetails
# Create your views here.

def cluster(request):
    """
    Retrieves the cluster information from the backend database
    """
    if request.method == "GET":
        cluster_list = []
        cluster_infos = ClusterDetails.objects.all()
        for count in cluster_infos:
            data = {
                'cluster_id': count.cluster_id,
                'cluster_name': count.cluster_name,
                'connection_id': count.connection_id,
                'user_id': count.user_id,
                'region': count.region,
                'backend_key': count.backend_key,
                'cluster_version': count.cluster_version,
                'disk_size': count.disk_size,
                'min_size': count.min_size,
                'max_size': count.max_size,
                'desired_size': count.desired_size,
                'instance_type': count.instance_type,
                'vpc_name': count.vpc_name,
                'vpc_id': count.vpc_id,
                'public_subnets': count.public_subnets,
                'private_subnets': count.private_subnets,
                'public_subnet_cidr': count.public_subnet_cidr,
                'private_subnet_cidr': count.private_subnet_cidr,
                'domain_names': count.domain_names,
                'cluster_endpoint': count.cluster_endpoint,
                'has_created': count.has_created,
                'lb_url': count.lb_url
            }
            cluster_list.append(data)
        return JsonResponse({"cluster": cluster_list}, status=200)