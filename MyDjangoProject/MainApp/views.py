from django.http import HttpResponse 
from sub_project.tokenizer import tokenize 
 
def index(request): 
    input_string ="MON-SAT 0800-1500 12 JAN 2024-14 JAN 2024 0800-1300 10 JAN 1300-1500 10 JAN 2024 1300-1500 MON, 10 JAN 2024 1400-1400 MON, 10 JAN 1400-2300"
    result = tokenize(input_string) 
    resultHTML = "Tokenizing \"" + input_string +"\" <br>Results:<br>"
    for match in result:
        resultHTML = resultHTML + match + "<br>"
    print(resultHTML)
    return HttpResponse(f" {resultHTML}") 
