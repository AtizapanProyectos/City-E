from django.contrib import admin
from django.urls import path
from maps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Autenticación y vistas principales
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login_alt'),
    path('logout/', views.logout_view, name='logout'),
    path('mapa/', views.mapa_view, name='mapa'),
    
    # APIs de datos electorales (Seccional y Global)
    path('api/seccion/<int:num_seccion>/', views.obtener_datos_seccion, name='api_seccion'),
    path('api/totales/', views.obtener_datos_totales, name='api_totales'),

    # APIs de gestión de Promovidos
    path('api/promovidos/', views.listar_promovidos, name='listar_promovidos'),
    path('api/cargar-promovidos/', views.cargar_promovidos, name='cargar_promovidos'),
    path('api/guardar-promovido/', views.guardar_promovido, name='guardar_promovido'),
    path('api/reiniciar-promovidos/', views.reiniciar_promovidos, name='reiniciar_promovidos'),
    
    # APIs de Escucha Social (3 candidatos)
    path('api/procesar-escucha/', views.procesar_escucha_social, name='procesar_escucha'),
    path('api/escucha-social/', views.obtener_escucha_social, name='obtener_escucha'),

    # APIs de gestión de Encuestas
    path('api/guardar-encuesta/', views.guardar_encuesta, name='guardar_encuesta'),
    path('api/eliminar-encuesta/', views.eliminar_encuesta, name='eliminar_encuesta'),
    path('api/reiniciar-encuestas/', views.reiniciar_encuestas, name='reiniciar_encuestas'),
    path('api/promedio-encuestas/', views.obtener_promedio_encuestas, name='promedio_encuestas'),
    path('api/historial-encuestas/', views.historial_encuestas, name='historial_encuestas'),
]