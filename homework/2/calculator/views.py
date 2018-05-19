from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

# context全部都是string，因为是django提取PARSE的，不管长什么样

# manually parameter validation in Django:
#NO.1 BUG:     you must check existence of a parameter before using it
# CORRECT : foo = request.POST.get('username') = null/value. It's dictionary.get()


def calculate(param, param1, param2):
    result = 'NaN'

    if param1 == 'NaN' or param1 == '':
        param1 = 0
    if param2 == 'NaN' or param2 == '':
        param2 = 0
    else:
        param1 = int(param1)
    if param2 == '':
        param2 = 0
    else:
        param2 = int(param2)

    if param == '=':
        return param2
    elif param == '+' or param == '':
        result = param1 + param2
    elif param == '-':
        result = param1 - param2
    elif param == '*':
        result = param1 * param2
    elif param == '/':
        if param2 == 0:
            return 'NaN'
        result = int(param1 / param2)
    return result


def isNum(param):
    try:
        int(param)
        return True
    except:
        return  False


def calculator(request ):
    context = {'cur_btn_num': '', 'result': '', 'pre_operation': '','num_screen':'0'}

    if 'cur_btn_num' in request.POST:
        if request.POST.get('cur_btn_num') == '' or isNum(request.POST.get('cur_btn_num')):
            context['cur_btn_num'] = request.POST['cur_btn_num']
        else:
            context = {'cur_btn_num': '', 'result': '', 'pre_operation': '', 'num_screen': 'NaN'}
            return render(request, 'calculator.html', context)

    if 'result' in request.POST:
        if request.POST.get('result') == '' or isNum(request.POST.get('result'))\
                or request.POST.get('result') == 'NaN':
            context['result'] = request.POST['result']
        else:
            context = {'cur_btn_num': '', 'result': '', 'pre_operation': '', 'num_screen': 'NaN'}
            return render(request, 'calculator.html', context)

    if 'pre_operation' in request.POST:
        if request.POST.get('pre_operation') == '' \
                or request.POST.get('pre_operation') == '+' \
                or request.POST.get('pre_operation') == '-' \
                or request.POST.get('pre_operation') == '*'\
                or request.POST.get('pre_operation') == '/'\
                or request.POST.get('pre_operation') == '=':
            context['pre_operation'] = request.POST['pre_operation']
        else:
            context = {'cur_btn_num': '', 'result': '', 'pre_operation': '', 'num_screen': 'NaN'}
            return render(request, 'calculator.html', context)

    if 'num_screen' in request.POST:
        if request.POST.get('num_screen') == '' or request.POST.get('num_screen') == 'NaN':
            context['num_screen'] = '0'
        elif isNum(request.POST.get('num_screen')):
            context['num_screen'] = request.POST['num_screen']
        else:
            context = {'cur_btn_num': '', 'result': '', 'pre_operation': '', 'num_screen': 'NaN'}
            return render(request, 'calculator.html', context)

    if 'button_op' in request.POST:
        if request.POST.get('button_op') == '' \
                or request.POST.get('button_op') == '+' \
                or request.POST.get('button_op') == '-' \
                or request.POST.get('button_op') == '*' \
                or request.POST.get('button_op') == '/' \
                or request.POST.get('button_op') == '=':
            context['result'] = calculate(context['pre_operation'], context['result'], context['num_screen'])
            context['num_screen'] = context['result']
            context['cur_btn_num'] = ''
            context['pre_operation'] = request.POST['button_op']
        else:
            context = {'cur_btn_num': '', 'result': '', 'pre_operation': '', 'num_screen': 'NaN'}
            return render(request, 'calculator.html', context)

    if 'button_num' in request.POST:
        if request.POST.get('button_num') == '' or isNum(request.POST.get('button_num')):
            context['cur_btn_num'] = context['cur_btn_num'] + request.POST['button_num']
            context['num_screen'] = int(context['cur_btn_num'])
        else:
            context = {'cur_btn_num': '', 'result': '', 'pre_operation': '', 'num_screen': 'NaN'}
            return render(request, 'calculator.html', context)

    return render(request, 'calculator.html', context)
