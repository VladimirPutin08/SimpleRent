# accounts/views.py
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

import traceback
import sys
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    """
    Wrapper around the normal CreateAPIView. If an exception happens,
    return a JSON response with the exception type and traceback so we
    can debug easily without shell access.
    """
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except Exception as exc:
            # Log it server-side too
            tb = "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
            logger.error("RegisterUserView exception: %s\n%s", str(exc), tb)

            # Return a JSON response with useful debug info (temporary)
            # NOTE: remove this debug behavior once we've fixed the bug.
            return Response(
                {
                    "ok": False,
                    "error": str(exc),
                    "exception_type": type(exc).__name__,
                    "traceback": tb.splitlines()[-25:],  # last 25 lines
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
