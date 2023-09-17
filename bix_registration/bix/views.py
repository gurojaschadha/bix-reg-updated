from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import BoatRegistration  # Add this import
from django.shortcuts import redirect


def welcome(request):
    return render(request, 'welcome.html')

@method_decorator(csrf_exempt, name='dispatch')
class BoatRegistrationView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            bix_id = data.get('bix_id')
            license_number = data.get('license_number')
            aadhar_number = data.get('aadhar_number')
            duration = data.get('duration')
            boat_type = data.get('boat_type')

            # Check for missing fields
            if not bix_id or not license_number or not aadhar_number or not duration or not boat_type:
                return JsonResponse({'error': 'All fields are required'}, status=400)

            # You can perform additional validation here

            registration = BoatRegistration(
                bix_id=bix_id,
                license_number=license_number,
                aadhar_number=aadhar_number,
                duration=duration,
                boat_type=boat_type,
            )
            registration.save()

            return JsonResponse({'message': 'Boat registered successfully'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
