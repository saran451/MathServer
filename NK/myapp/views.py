from django.shortcuts import render

def churn_rate(request):
    l = float(request.POST.get('initial_cust', '0'))
    i = float(request.POST.get('present_cust', '0'))

    churnrate = (l/i)*100 if request.method == 'POST' and i != 0 else 0

    print("InitialCustomer =", l)
    print("PresentCustomer=", i)
    print("Churnrate =", churnrate)

    return render(
        request,
        'myapp/math.html',
        {'l': l, 'i': i, 'churnrate': churnrate}
    )