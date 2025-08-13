# Comment importer le module de facture personnalisé via Odoo Studio

Ce guide explique comment utiliser le module fourni dans le dossier `studio_invoice_report` pour personnaliser vos factures sur Odoo Online.

Le principe est simple : nous allons compresser le dossier en un fichier `.zip`, puis l'importer dans Odoo Studio.

## Étapes

### 1. Compresser le dossier du module

1.  Sur votre ordinateur, localisez le dossier `studio_invoice_report`.
2.  Faites un clic droit sur ce dossier.
3.  Choisissez **Envoyer vers > Dossier compressé (zippé)**. (Le nom peut varier légèrement selon votre système d'exploitation).
4.  Cela créera un fichier nommé `studio_invoice_report.zip`. C'est ce fichier que nous allons importer.

    

### 2. Importer le module dans Odoo Studio

1.  Connectez-vous à votre base de données Odoo Online.
2.  Ouvrez **Odoo Studio** en cliquant sur l'icône de clé à molette en haut à droite.
3.  Dans le menu de personnalisation de Studio, cliquez sur **Import / Export** > **Importer**.

    

4.  Une fenêtre s'ouvre. Cliquez sur **"Téléchargez votre fichier .zip"**.
5.  Sélectionnez le fichier `studio_invoice_report.zip` que vous venez de créer.
6.  Cliquez sur le bouton **IMPORTER**.

    

Odoo va maintenant importer votre module. Cela peut prendre quelques instants. Une fois terminé, la page se rechargera.

### 3. Tester le résultat

C'est terminé ! Le module est installé et le rapport de facture est modifié.

1.  Quittez Odoo Studio en cliquant sur **FERMER**.
2.  Allez dans le module **Comptabilité**.
3.  Ouvrez une facture et imprimez-la.

Le nouveau design, fidèle à votre image, devrait s'afficher.

### En cas de problème

- Si l'importation échoue, assurez-vous que vous avez bien compressé le dossier `studio_invoice_report` et non les fichiers qu'il contient directement.
- Pour désactiver le module, allez dans le menu **Applications**, retirez le filtre "Apps", recherchez `Rapport de Facture Personnalisé (Studio)` et désinstallez-le.
