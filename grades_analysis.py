#mportez la bibliothèque numpy et créez le tableau « grades » comme spécifié ci-dessus.
import numpy as np
grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print(grades)

#Utilisez les fonctions numpy pour calculer la moyenne, la médiane et l’écart type des notes.
mean_grade = np.mean(grades)
print(f"la moyenne est:",mean_grade)

median_grade = np.median(grades)
print(f"la mediane est:",median_grade)

std_grade = np.std(grades)
print(f"l'ecart-type est:",std_grade)

#Utilisez la fonction numpy pour trouver le maximum et le minimum des notes.
max_grade = np.max(grades)
print(f"la note maximale est",max_grade)

min_grade = np.min(grades)
print(f"la note maximale est",min_grade)

#Utilisez la fonction numpy pour trier les notes par ordre croissant.
sorted_grades = np.sort(grades)
print(f"les notes triées par ordre croissant sont:",sorted_grades)

#Utilisez la fonction numpy pour trouver l'index de la note la plus élevée dans le tableau.
max_index = np.argmax(grades)
print(f"l'index de la note maximale  est :",max_index)

#Utilisez la fonction numpy pour trouver l'index de la note la plus basse dans le tableau.
min_index = np.argmin(grades)
print(f"l'index de la note minimale  est :",min_index)

#Utilisez la fonction numpy pour calculer la somme des notes.
sum_grade = np.sum(grades)
print(f"l'index de la note minimale  est :",np.argmin(grades))

#Utilisez la fonction numpy pour compter le nombre d'étudiants ayant obtenu un score supérieur à 90.
count1 = np.sum(grades>90)
print(f"le nombre d'étudiants ayant obtenu une note  supérieur à 90 est:",count1)

#Utilisez la fonction numpy pour calculer le pourcentage d'étudiants ayant obtenu un score supérieur à 90.
#pourcent = np.sum(grades>90)/len(grades>90)*100
percent = np.mean(grades>90)*100
print(f"le pourcentage d'étudiants ayant obtenu une note  supérieur à 90 est:",pourcent)

#Utilisez la fonction numpy pour calculer le pourcentage d'étudiants ayant obtenu un score inférieur à 75.
pourcent1 = np.sum(grades>75)/len(grades>75)*100
print(f"le pourcentage d'étudiants ayant obtenu une note  supérieur à 75 est:",pourcent1)

#Utilisez la fonction numpy pour extraire toutes les notes supérieures à 90 et les placer dans un nouveau tableau appelé « high_performers ».

high_performers = grades[grades>90]
print(f"les notes supérieures à 90 sont:",high_performers)

#Créez un nouveau tableau appelé « passing_grades » qui contient toutes les notes supérieures à 75.
passing_grades = grades[grades >= 75]
print(f"les notes supérieures à 75 sont:",passing_grades)



