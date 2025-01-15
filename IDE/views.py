from django.http import JsonResponse,HttpResponse

from django.shortcuts import render
from .forms import PYTHON_IDE
from .compiler import Compiler
from .utility import list_files_and_folders
def home_page(request):
    
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        code = request.POST.get("code", "")
        if code:
            with open("static/newfile.py","w") as f:
                temp = code.split("\n")
                f.writelines(temp)
            Com = Compiler(code)
            Com.run()
            output = Com.output()
        return JsonResponse({'output': output})
    with open("static/newfile.py","r") as f:
        data = f.readlines()
    data = "".join(data)
    direc = list_files_and_folders('static/FILES')
    df ={"data":data,'structure':direc}
    print(df)
    
  
    
    return render(request, "index.html",)
