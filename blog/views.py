from django.shortcuts import render
from arrow import Arrow
# Create your views here.
def index(req):
    time=Arrow.now().format("YYYY年-MM月-DD日 HH时:mm分:ssZZ秒")
    return render(req,'index.html',{'time':time})