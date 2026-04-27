import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # 1. استيراد البيانات من ملف CSV
    df = pd.read_csv('epa-sea-level.csv')

    # 2. إنشاء مخطط التشتت (Scatter Plot)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # 3. إنشاء خط أفضل مطابقة الأول (باستخدام كل البيانات)
    # نحسب الانحدار الخطي من البداية حتى آخر سنة موجودة
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # ننشئ مصفوفة سنوات تمتد من 1880 إلى 2050 للتنبؤ بالمستقبل
    x_pred = pd.Series([i for i in range(1880, 2051)])
    # معادلة الخط المستقيم: y = mx + c
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, 'r', label='Best Fit Line 1')

    # 4. إنشاء خط أفضل مطابقة الثاني (بيانات عام 2000 فما فوق)
    # نفلتر البيانات لنأخذ فقط من سنة 2000 إلى أحدث سنة
    new_df = df[df['Year'] >= 2000]
    res_recent = linregress(new_df['Year'], new_df['CSIRO Adjusted Sea Level'])
    
    # ننشئ مصفوفة سنوات من 2000 إلى 2050
    x_pred_recent = pd.Series([i for i in range(2000, 2051)])
    y_pred_recent = res_recent.slope * x_pred_recent + res_recent.intercept
    plt.plot(x_pred_recent, y_pred_recent, 'green', label='Best Fit Line 2')

    # 5. إضافة العناوين والمسميات للمخطط
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # حفظ الصورة والعودة بها
    plt.savefig('sea_level_plot.png')
    return plt.gca()
