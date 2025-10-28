from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def reset_user_password(request, user_id):
    """
    View to reset another user's password.
    Only users with the 'supperadmin' staff_category can perform this action.
    """
    # Ensure the logged-in user has permission to reset passwords.
    if not request.user.can_reset_password():
        return HttpResponseForbidden("You are not allowed to reset passwords for other users.")
    
    user_to_reset = get_object_or_404(User, id=user_id)
    
    # Here you could either generate a new password or
    # redirect to a password reset form.
    # For demonstration, we simply set a default password:
    new_password = "newdefaultpassword"  # Replace with a secure method.
    user_to_reset.set_password(new_password)
    user_to_reset.save()
    
    messages.success(request, f"Password for {user_to_reset.email} has been reset.")
    return redirect('admin_user_list')  # Replace with your actual redirect URL.
