Myshop:
Compte-rendu: 


1•Estimation du temps nécessaire pour coder l'applictaion:
    Après la lecture de l'énoncé, j'ai commencé par schématiser la structure de mon projet, 
ses composantes et les tâches à accomplir pour aboutir au résultat final. 

Mon projet représente un magasin et contient une application "products" qui représente l'ensemble
des produits du magasin. 
Un produit est représenté par : sa marque, sa nature, son code-barres, sa date d'expiration. 
J'ai aussi prévu le champ slug(de type SlugField; (voir utilisation ci-dessous))

Les tâches à effectuer sont : 
    
    •Créer une base de donnnées PostgreSQL, un utilisateur qui pourra avoir accès à la base de données.
    
    •Créer le répertoire de mon projet, activer l'environnement numérique et configurer PyCharm.
    
    •Afficher la liste de mes produits avec la date d'expiration.
    
    •Créer une application, et définir mon modèle, appliquer les modifications nécessaires dans settings.py.
    
    •Créer un super utilisateur et pouvoir accéder à l'interface d'administration.
    
    •Faire les migrations pour ajouter la table de mon modèle à la base de données
    
    •Ajouter un nouveau produit.
    
    •Mettre à jour une date d'expiration.
    
    •Supprimer un produit de la liste des produits.
    
    •Vérifier que le produit que je souhaite créer n'existe pas. S'il existe déjà, mettre 
    à jour sa date d'expiration. 
    
    •Mettre d'éventuels liens pour rendre la navigation fluide.
    
    •Styliser mon application avec du CSS.
    
J'estime que l'ensemble des tâches pourrait me prendre environ 6h. 


2•Structure du projet: 
Dans le fichier src, il y a deux autres fichiers : myshop et products. 

    •myshop : ici, c'est le répertoire de mon projets. Il y a le template pour afficher l'accueil de mon magasin,
    et un lien vers la liste des produits.
    
    •products : ce répertoire représente l'application. 
    =>views.py :
        ShopHome(ListView) : grâce à ListView je peux récupérer tous les produits dans la base de données
        dans uen sorte de queryset. Je donne un nom à ce queryset pour pouvoir le récupérer dans product_list.html qui affichela liste des produits.
        
        CreateProduct(CreateView) : Ajoute la possibilité de créer un produit avec un formulaire qui sera affiché
        dans la page product_create.html. Quand je crée un objet, je me redirige automatiquement vers la page de la liste de mes produits.
        
        ProductDetail(DetailView) : En cliquant sur un produit, on se dirige vers la page product_list.html,
        qui affiche plus de détails sur le produit.
        
        ProductUpdate(UpdateView)  : Mettre à jour la date d'expiration d'un produit et cela en récupérant son "slug"
        
        DeleteProduct(DeleteView) : Suuprimer un produit en récupérant également son slug 
        
        Remarque : le slug prend la valeur du gtin. 
                   en l'introduisant dans les urls définis dans urls.py, je peux récupérer un produit avec et le modifier ou le supprimer.
                   
    => urls.views :
    Comprend les différents liens vers les différentes vues créées dans views.py. 
    
    =>En étant sur la page de la liste des produits, je peux aisément ajouter, supprimer et mettre à jour les produits
    grâce aux liens que j'ai créés dans les templates.
    
    

    
3  •Pour accéder à l'application, il faut se mettre dans le dossier /myshop/src et lancer la commande :

   python manage.py runserver ensuite aller sur l'accueil du magasin à l'adresse : http://127.0.0.1:8000/ .
   
   •Accéder à l'interface d'administration sur la page http://127.0.0.1:8000/admin avec les identifiants suivants:
        Nom d'utilisateur : Fatima
        Mot de passe : Codabene
        
        
4•Difficultés rencontrées lors de la programmation de l'application :

•Problème technique lors de l'installation la bibliothèque psycopg2.

•J'ai eu des difficultés pour finir les tâches que j'ai prévues. En effet, lorsque j'essaie d'ajouter un 
produits déjà existant, je n'arrive pas mettre à jour sa date d'expiration. Après plusieurs recherches, 
je pense que je peux remédier à cela en surchargeant la méthode CreateProduct. 




        
        
        
    