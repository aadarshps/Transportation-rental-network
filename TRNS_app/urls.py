from django.urls import path

from TRNS_app import views, admin_views, customer_views, ownerviews

urlpatterns = [
    path('',views.home,name='home'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('customer_reg',views.customer_reg,name='customer_reg'),
    path('adminpage',views.adminpage,name='adminpage'),
    path('customerpage',views.customerpage,name='customerpage'),
    path('owner_reg',views.owner_reg,name='owner_reg'),
    path('ownerpage',views.ownerpage,name='ownerpage'),
    path('logout_view',views.logout_view,name='logout_view'),


    path('view_customers',admin_views.view_customers,name='view_customers'),
    path('approve_cus/<int:id>/',admin_views.approve_cus,name='approve_cus'),
    path('del_cus/<int:id>/',admin_views.del_cus,name='del_cus'),
    path('vehicle_view',admin_views.vehicle_view,name='vehicle_view'),
    path('del_vehicle/<int:id>/',admin_views.del_vehicle,name='del_vehicle'),
    path('bookings',admin_views.bookings,name='bookings'),
    path('confirm_booking/<int:id>/',admin_views.confirm_booking,name='confirm_booking'),
    path('reject_booking/<int:id>/',admin_views.reject_booking,name='reject_booking'),
    path('chat_add_ad',admin_views.chat_add_ad,name='chat_add_ad'),
    path('chat_view_admin',admin_views.chat_view_admin,name='chat_view_admin'),
    path('Feedback_CUS',admin_views.Feedback_CUS,name='Feedback_CUS'),
    path('reply_Feedback/<int:id>/',admin_views.reply_Feedback,name='reply_Feedback'),
    path('view_owners',admin_views.view_owners,name='view_owners'),
    path('approve_owe/<int:id>/',admin_views.approve_owe,name='approve_owe'),
    path('del_owe/<int:id>/',admin_views.del_owe,name='del_owe'),
    path('Payment',admin_views.Payment,name='Payment'),
    path('Payment_view',admin_views.Payment_view,name='Payment_view'),


    path('view_vehi',customer_views.view_vehi,name='view_vehi'),
    path('book_vehicle',customer_views.book_vehicle,name='book_vehicle'),
    path('booking_status',customer_views.booking_status,name='booking_status'),
    path('chat_add_cus',customer_views.chat_add_cus,name='chat_add_cus'),
    path('chat_view_cus',customer_views.chat_view_cus,name='chat_view_cus'),
    path('Feedback_add_user',customer_views.Feedback_add_user,name='Feedback_add_user'),
    path('Feedback_view_user',customer_views.Feedback_view_user,name='Feedback_view_user'),
    path('pay_rent_fee',customer_views.pay_rent_fee,name='pay_rent_fee'),
    path('payment_view',customer_views.payment_view,name='payment_view'),
    path('viewAds',customer_views.viewAds,name='viewAds'),


    path('vehicle_add',ownerviews.vehicle_add,name='vehicle_add'),
    path('vehicle_view_ow',ownerviews.vehicle_view_ow,name='vehicle_view_ow'),
    path('update_vehicles/<int:id>/',ownerviews.update_vehicles,name='update_vehicles'),
    path('del_vehicle_ow/<int:id>/',ownerviews.del_vehicle_ow,name='del_vehicle_ow'),
    path('booking_view',ownerviews.booking_view,name='booking_view'),
    path('Ad_payment',ownerviews.Ad_payment,name='Ad_payment'),
]