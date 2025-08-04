# formdata/views.py

from rest_framework import generics
from rest_framework.response import Response
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

class WheelSpecificationListCreateAPIView(generics.ListCreateAPIView):
    queryset = WheelSpecification.objects.all().order_by('-submittedDate')
    serializer_class = WheelSpecificationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        formNumber = self.request.query_params.get('formNumber', None)
        submittedBy = self.request.query_params.get('submittedBy', None)
        submittedDate = self.request.query_params.get('submittedDate', None)
        
        if formNumber:
            queryset = queryset.filter(formNumber=formNumber)
        if submittedBy:
            queryset = queryset.filter(submittedBy=submittedBy)
        if submittedDate:
            queryset = queryset.filter(submittedDate=submittedDate)
            
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        # Customize the response to match the Postman collection
        response_data = {
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": serializer.data['formNumber'],
                "submittedBy": serializer.data['submittedBy'],
                "submittedDate": serializer.data['submittedDate'],
                "status": "Saved"
            }
        }
        return Response(response_data, status=201)