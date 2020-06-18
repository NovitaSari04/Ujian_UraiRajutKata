# Soal Ujian Python Data Science Fundamental

![Lintang_Purwadhika](https://static.wixstatic.com/media/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png/v1/fill/w_246,h_39,al_c,usm_0.66_1.00_0.01/2e6af2_f69a4271c3534ae1869a7ed63e278b2b~mv2.png)

<hr>

### **Soal 1 - 🆒 Mengurai & Merajut Kata**

Buatlah sebuah __file python (*.py*)__ yang berisi sebuah __class__ dengan __2 buah method__, yaitu __urai(*string*)__ dan __rajut(*string*)__. Dengan __class__ tersebut, buatlah sebuah __object__ yang dapat digunakan untuk mengurai & merajut sebuah __string__.

```python
# buat sebuah class dengan 2 method
class uraiRajutKata:
    def urai(...):
        ...
    def rajut(...):
        ...

# buat sebuah object
x = uraiRajutKata()
```

- Method __urai(*string*)__ akan mengurai string. Adapun cara pemanggilan method __urai(*string*)__ dan contoh output yang diharapkan adalah sebagai berikut:

    ```python
    print(x.urai('Code'))
    print(x.urai('Python'))
    print(x.urai('Purwadhika'))

    # Output:
    CCoCodCode
    PPyPytPythPythoPython
    PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika
    ```

- Sedangkan method __rajut(*string*)__ akan merajut kembali string yang terurai menjadi bentuk kata asalnya. Adapun cara pemanggilan method __rajut(*string*)__ dan contoh output yang diharapkan adalah sebagai berikut:

    ```python
    print(x.rajut('CCoCodCode'))
    print(x.rajut('PPyPytPythPythoPython'))
    print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
    
    # Output:
    Code
    Python
    Purwadhika
    ```

