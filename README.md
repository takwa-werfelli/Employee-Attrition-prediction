# Prédiction de l'Attrition des Employés

Ce projet a pour objectif de prédire si un employé est susceptible de quitter l'entreprise à l’aide de techniques de Machine Learning. Il est basé sur un jeu de données RH contenant plusieurs caractéristiques liées à l’environnement de travail, la satisfaction des employés, et leur rémunération.  
Les données utilisées dans ce projet proviennent du jeu de données disponible sur Kaggle :  
🔗 [Jeu de données IBM HR Analytics sur Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

---

## 2. Technologies utilisées

- **Python**  
- **Pandas, NumPy** : manipulation des données  
- **Scikit-learn** : machine learning et évaluation  
- **Matplotlib, Seaborn** : visualisation des données  
- **Joblib** : sauvegarde et chargement du modèle  
- **HTML / CSS** : création et mise en forme de l'interface utilisateur

---

## Contenu du projet

- Exploration et nettoyage des données  
- Analyse visuelle des variables  
- Détection et traitement des valeurs aberrantes  
- Encodage des variables catégorielles  
- Sélection des variables pertinentes  
- Entraînement de plusieurs modèles de classification  
- Évaluation de la performance  
- Sauvegarde et chargement du modèle  
- Prédiction sur de nouvelles données

---

## Modèles utilisés

Quatre modèles de classification ont été testés :

- Régression Logistique  
- k-Nearest Neighbors (KNN)  
- Arbre de Décision  
- Random Forest  

Le modèle final retenu est la **Régression Logistique**, sélectionnée pour sa simplicité, sa performance et sa capacité à être interprétée.

---

## Attributs utilisés dans le modèle

Voici les variables sélectionnées pour entraîner le modèle final :

- `OverTime` : Indique si l'employé effectue des heures supplémentaires (Oui/Non)  
- `MaritalStatus` : Statut marital (Célibataire, Marié, Divorcé)  
- `JobInvolvement` : Niveau d'implication dans le travail (score de 1 à 4)  
- `YearsAtCompany` : Nombre total d’années passées dans l'entreprise  
- `StockOptionLevel` : Niveau de stock-options attribué à l’employé  
- `YearsWithCurrManager` : Nombre d'années sous la responsabilité du manager actuel  
- `Age` : Âge de l’employé  
- `MonthlyIncome` : Revenu mensuel brut  
- `YearsInCurrentRole` : Ancienneté dans le poste actuel  
- `JobLevel` : Niveau hiérarchique dans l'organisation  
- `TotalWorkingYears` : Nombre total d'années d’expérience professionnelle

---

## Prétraitement des données

- Suppression des colonnes inutiles (`EmployeeCount`, `StandardHours`, `Over18`, `EmployeeNumber`)  
- Analyse des valeurs aberrantes avec les boxplots  
- Traitement des outliers sur `MonthlyIncome` via la méthode IQR  
- Encodage des variables catégorielles avec `LabelEncoder`  
- Visualisation des corrélations pour la sélection des variables les plus influentes

---

## Installation et utilisation

### 1. Cloner le dépôt

```bash
git clone https://github.com/takwa-werfelli/Employee-Attrition-prediction.git
cd Employee-Attrition-prediction
