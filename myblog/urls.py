from django.urls import path, include
from django.views.generic import RedirectView  # 新增这一行

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', RedirectView.as_view(url='/blog/', permanent=True)), # 让首页自动跳转到 blog
]