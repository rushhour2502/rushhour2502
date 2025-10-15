def squares (x):
    result =[]
    for i in x:
        c = i**2
        result.append(c)
    for j in result:
        print (j)
    print (f"""
    this is the sum of squares: {sum(result)}
    this is the sum of values: {sum(x)}
        """)
x = [
    51, 52, 50, 53, 50
    ]
squares(x)

# %%
v=[]

def remove_sp(list):
    x = c.replace("\n", " ").lower()
    x = x.split()
    x.sort()
    print (x)

# %%
    for i in x:
        v.append(i)
    v.sort()
    return v

#%%
c = """Breast feeding
Inflammation
Hypercholesterolemia
Diabetes
Fenugreek boosts testosterone
Weight loss
Blood sugar control
Constipation
Heart Disease
Aids digestion
Antioxidant potential
Appetite control
Cancer
Fever
Heartburn
Menstrual cramps
Polycystic ovary syndrome
Anticancer potential
Antidiabetic potential
Baldness
Hypocholesterolemia
Improved hair health
Improved skin health
Improves sex drive
"""




# %%
remove_sp(c)
# %%
