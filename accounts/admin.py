from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    تخصيص عرض نموذج المستخدم في لوحة تحكم Django.
    """
    model = CustomUser
    # list_display = (
    #     "email",
    #     "username",
    #     "first_name",
    #     "last_name",
    #     "invited_by",
    #     "invited_count",
    #     "premium_features",
    #     "is_staff",
    # )
    # fieldsets = UserAdmin.fieldsets + (
    #     (
    #         "بيانات إضافية",
    #         {
    #             "fields": (
    #                 "invited_by",
    #                 "referral_code",
    #                 "invited_count",
    #                 "premium_features",
    #             )
    #         },
    #     ),
    # )
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (
    #         "بيانات إضافية",
    #         {
    #             "fields": (
    #                 "email",
    #                 "first_name",
    #                 "last_name",
    #                 "invited_by",
    #                 "referral_code",
    #             )
    #         },
    #     ),
    # )

# # تسجيل النماذج في لوحة تحكم Django
admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Invitation, InvitationAdmin)
# admin.site.register(AppVersion, AppVersionAdmin)