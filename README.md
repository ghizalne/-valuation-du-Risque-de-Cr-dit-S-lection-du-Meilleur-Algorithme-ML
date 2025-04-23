# -valuation-du-Risque-de-Cr-dit-S-lection-du-Meilleur-Algorithme-ML
Évaluation du Risque de Crédit : Comparaison et Sélection du Meilleur Algorithme de Machine Learning pour une Performance Optimale
# Classification du Risque de Crédit

Ce projet est un système de prédiction du risque de crédit développé dans le cadre du module de Data Mining à l’Université Mohammed Premier. Il vise à prédire si un client présente un risque de défaut de paiement à partir de ses informations personnelles et financières.

## 🔍 Objectif

Développer un modèle de machine learning pour classifier les demandes de crédit en deux catégories :
- Risque de crédit élevé (1)
- Risque de crédit faible (0)

## 🧰 Technologies et Bibliothèques utilisées

- **Python** – Langage principal
- **Google Colab** – Environnement d'exécution
- **Streamlit** – Interface utilisateur pour le déploiement
- **Scikit-learn** – Modèles de machine learning
- **Pandas, Numpy** – Manipulation de données
- **Matplotlib, Seaborn** – Visualisation
- **Pickle** – Sauvegarde des modèles

## 📁 Dataset

Le dataset utilisé contient 665 instances, chacune représentant une demande de crédit avec des attributs comme :
- Genre, Statut matrimonial, Niveau d'éducation, Revenus, Historique de crédit, Zone géographique, etc.

## 🔄 Pipeline du Projet

Le projet suit la méthodologie **CRISP-DM** :
1. **Compréhension métier**
2. **Compréhension des données**
3. **Préparation des données**
4. **Modélisation** (KNN, Decision Tree, Random Forest, Naive Bayes, Régression Logistique)
5. **Évaluation** (Accuracy, MCC, Matrice de confusion)
6. **Déploiement avec Streamlit**

## ✅ Résultats

L'algorithme le plus performant était **Naive Bayes**, avec :
- Accuracy : 80%
- MCC : 0.61

## 🚀 Lancement de l’application

Pour exécuter l’application Streamlit :

```bash
streamlit run main.py

