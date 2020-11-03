from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password


def forgot_password(request):
	return render(request, 'forgot-password.html')


def forgot_password_ajax(request):
	if request.is_ajax():
		old_password = request.POST.get('old_password', None)
		new_password = request.POST.get('new_password', None)
		confirm_password = request.POST.get('confirm_password', None)


		user = request.user # we need to get current logged in user

		if user.check_password(old_password): # this is default password check if match with DB
			upper_case = sum(1 for c in new_password if c.isupper())
			digits = sum(1 for c in new_password if c.isdigit())
			chars = sum(1 for c in new_password if not c.isalnum())
			length = len(new_password)


			if confirm_password != new_password:
				response = {'error': 'Password mismatch. Try again.'}
				return JsonResponse(response)
			elif length < 6:
				response = {'error': 'New Password is too short. Try another'}
				return JsonResponse(response)
			elif not upper_case:
				response = {'error': 'New Password must contain at least one Uppercase.'}
				return JsonResponse(response)
			elif not digits:
				response = {'error': 'New Password must contain at least one number.'}
				return JsonResponse(response)
			elif not chars:
				response = {'error': 'New Password must contain at least one character.'}
				return JsonResponse(response)

			user.set_password(new_password) # This will auto hash the password.
			user.save() # this will save to DB
			if user.save():
				response = {'success': 'Password updated successfully'}
				return JsonResponse(response)
			else:
				response = {'error': 'Error. Please try again.'}
				return JsonResponse(response)
		else:
			response = {'error': 'We could not understand your request.'}
			return JsonResponse(response)

