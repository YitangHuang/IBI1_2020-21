# got helped by CSDN communication and my classmates.
# Especially thanks to Wang juanle, Lu jianzhang, Wang yufei.
# referrence:
# https://www.runoob.com/python/python-xml.html
# https://blog.csdn.net/kongsuhongbaby/article/details/84869838
# https://blog.csdn.net/qq_37174526/article/details/89489212

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from xml.dom.minidom import parse
import xml.dom.minidom                         # import the packages we need
DOMTree=xml.dom.minidom.parse('E:/github repo/IBI1_2020-21/practical 14/go_obo.xml')
a = DOMTree.documentElement
terms = a.getElementsByTagName('term')
id={}
# use a dictionary so we can store more value at one time. Idea from my classmate. Especially thanks to Wang Juanle.

for n in terms:
    is_a = n.getElementsByTagName('is_a')
    go_id = n.getElementsByTagName('id')[0]
    for i in is_a:
        if i.childNodes[0].data in id:
            id[i.childNodes[0].data].append(go_id.childNodes[0].data)
        else:
            id[i.childNodes[0].data]=[go_id.childNodes[0].data]

# #  initialize the 4 list we need.
RNA_list=[]
protein=[]
carbohydrate=[]
DNA_list=[]
for n in range (terms.length):
    if 'DNA' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
        DNA_list.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)

for n in range (terms.length):
    if 'RNA' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
        RNA_list.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)

for n in range (terms.length):
    if 'protein' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
        protein.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)


for n in range (terms.length):
    if 'carbohydrate' in terms[n].getElementsByTagName('defstr')[0].childNodes[0].data:
        carbohydrate.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)

def nodenumber(idis,molelist):
    child=[]
    for i in molelist:
        if i in idis:
            childnode=idis[i]
            child+=childnode
            child+=nodenumber(idis,childnode)
    return child

def len_calculator(id, list):
    result = len(set(nodenumber(id,list)))
    # set() can delete all the repeated elements
    return result

# use a function to get the result in a more simplified way
DNA_length=len_calculator(id,DNA_list)
RNA_length=len_calculator(id, RNA_list)
protein_length=len_calculator(id, protein)
carbohydrate_length=len_calculator(id, carbohydrate)

# Make a bar graph
name_list = ['DNA', 'RNA', 'protein', 'carbohydrate']
num_list = [DNA_length, RNA_length, protein_length,carbohydrate_length]
plt.bar(range(len(num_list)),num_list, tick_label = name_list)
plt.title('ChildNotes Numbers')
plt.show()

# Make a pieplot
labels='DNA', 'RNA', 'protein', 'carbohydrate'
sizes=[DNA_length, RNA_length, protein_length, carbohydrate_length]
explode=(0.1, 0.1, 0.1, 0.1)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
plt.title(' Percentage of childNodes')
plt.show()
# ------------------------------------CRITICAL THINKING---------------------------------------------------------------
# # define a function to get 4 lists we need in a easy way.
# type = ''
# def id_calculator (list,type):      # type is a string, so don't forget to type''
#     for n in range(terms.length):
#         if type in terms[n].getElementsByTagName('defstr')[0].childNodes[0]:
#             list.append(terms[n].getElementsByTagName('id')[0].childNodes[0].data)
#     return list
# DNA_list = id_calculator(DNA_list,"\'DNA\'")
# RNA_list = id_calculator(RNA_list,"\'RNA\'")
# protein = id_calculator(protein,"\'Protein\'")
# carbohydrate = id_calculator(carbohydrate,"\'carbohydrate\'")

# #TypeError: argument of type 'Text' is not iterable

# I want to use a function to simplify my code, but I keep recieve the error messange. I think the problem is mainly in the type of 'DNA', 'RNA' and stuff.
# Maybe I can't use these way because I can't use string to index the information I want.
# If so, could you inform me if you have a better solution to my problem in the feedback session?
# Thank you every much !