from flask import Flask,render_template, request, flash, session, abort
#from flask_mysqldb import MySQL
import pymysql

import os
#-------------------- Connexion à la base ---------------------------------------- 
app = Flask(__name__)
app.secret_key = "super secret key"

db = pymysql.connect(host = '127.0.0.1',user = 'root',passwd = 'root',db = 'flask') 
#db=pymysql.connect('127.0.0.1','root','root','db');


#---------------------- Page d'authentification ------------------------------------------

@app.route('/')
def home():
    return render_template('auth.html')
@app.route('/login', methods = ['POST', 'GET'])
def login():
     
    if request.method == 'POST':
        name = request.form['login']
        pas = request.form['password']
        cursor = db.cursor()
        cursor.execute(''' select * from admin where login=%s and passwrd=%s''',(name,pas))
        data=cursor.fetchone()
		
        cursor.close()
		
        
        if  data:
        	session['logged_in'] = True
        	return render_template('acceuil.html')
        else:
        	flash('wrong password!')
        	return render_template('auth.html')
        	#******* Déconnexion *******
@app.route('/logout')
def  logout():
	session['logged_in'] = False
	return render_template('auth.html')
#-------------------- Page d'acceuil ----------------------------------------
    
    
@app.route('/acceuil.html') 
def acceuil():
	return render_template('acceuil.html')
#------------------- Page de gestion des modules ----------------------------

    
@app.route("/module.html")
def module():
	
	return render_template("module.html")	

#----------------- Page d'ajout du module -----------------------------------
    
@app.route('/ajoutermodule.html')
def ajoutermodule():
    return render_template('ajoutermodule.html')
    
@app.route('/ajoutermod',methods = ['POST', 'GET'])
def ajoutermod():
	if request.method == 'POST':
		nom = request.form['nom']
		code = request.form['code']
		cursor = db.cursor()
		cursor.execute(''' INSERT INTO  module(code,nom) VALUES(%s,%s) ''',(code,nom))
		db.commit()
		cursor.close()
		return render_template("res.html",msg="Module ajouté avec succées") 

    
#----------------- Page de modification du module ----------------------------
    
@app.route('/modifiermodule.html')
def modifiermodule():
		
		cursor = db.cursor()
		cursor.execute(''' select * from module''')
		data = cursor.fetchall()
		cursor.close()
		return render_template("modifiermodule.html",userDetails=data)

@app.route('/modifiermod',methods = ['POST', 'GET'])
def modifiermod():
	if request.method == 'POST':
		nom = request.form['nom']
		code = request.form['code']
		cursor = db.cursor()
		cursor.execute(''' UPDATE  module SET  nom=%s where code=%s''',(nom,code))
		db.commit()
		cursor.close()
		return render_template("res.html",msg="Module modifié avec succées")  

#------------------- Supprimer une module -----------------------------------		
@app.route('/supprimermodule.html')
def supprimermodule():
	cursor = db.cursor()
	cursor.execute(''' select * from module''')
	data = cursor.fetchall()
	cursor.close()
	return render_template('supprimermodule.html',userDetails=data)
    
@app.route('/supprimermod',methods = ['POST', 'GET'])
def supprimermod():
	if request.method == 'POST':
		
		code = request.form['code']
		cursor = db.cursor()
		cursor.execute(''' DELETE FROM  module where  code=%s''',([code]))
		db.commit()
		cursor.close()
		return render_template("res.html",msg="Module supprimé avec succées")  
		
#--------------------- Consulter les modules ---------------------------
@app.route('/consultermodule.html')
def consultermodule():
	cursor = db.cursor()
	cursor.execute(''' select * from module''')
	data = cursor.fetchall()
	cursor.close()
	return render_template('consultermodule.html',userDetails=data)
	 
#-------------------  Page du gestion des matieres -------------------
@app.route("/matiere.html")
def matiere():
	
	return render_template("matiere.html")	
	
#------------------- Ajout d'une matiere -------------------------------	
@app.route("/ajoutermatiere.html")
def ajoutermatiere():
	cursor = db.cursor()
	cursor.execute(''' select * from specialite''')
	data = cursor.fetchall()
	cursor.execute(''' select * from module''')
	mod = cursor.fetchall()
	return render_template("ajoutermatiere.html",userDetails=data,mod=mod)
	
@app.route('/ajoutermat', methods = ['POST', 'GET'])
def ajoutermat():
	if request.method == 'POST':
		nom = request.form['nom']
		classe = request.form['cl']
		coeff = request.form['coeff']
		code = request.form['code']
		specialite = request.form['specialite']
		typee = request.form['type']
		sem = request.form['sem']
		codem = request.form['codem']
		cursor = db.cursor()
		cursor.execute(''' INSERT INTO matieres VALUES(%s,%s,%s,%s,%s,%s,%s,%s)''',(code,nom,classe,specialite,sem,typee,coeff,codem))
		db.commit()
		cursor.close()
		return render_template("res.html",msg="Matière ajouté avec succées") 

	
	
#------------------- Modification d'une matiere -----------------------	
@app.route("/modifiermatiere.html")
def modifiermatiere():
		return render_template("modifiermatiere.html")


@app.route('/modifiermat', methods = ['POST', 'GET'])
def modifiermat():
	if request.method == 'POST':
		nom = request.form['nom']
		sem = request.form['sem']
		code = request.form['code']
		cursor = db.cursor()
		cursor.execute('''select * from matieres where code=%s''',[code])
		data = cursor.fetchone()
		if data:
			cursor = db.cursor()
			cursor.execute(''' update  matieres set nom=%s and semestre=%s where code=%s''',(nom,sem,[code]))
			db.commit()
			msg="Matiere modifié avec succes"
		else:
			msg="Code matiere inexistant"
		cursor.close()
		return render_template('res.html',msg=msg)
		
		
	

#---------------- Consulter la liste des matieres ----------------------	
@app.route("/consultermatiere.html")
def consultermatiere():
	cursor = db.cursor()
	cursor.execute(''' select m.*, s.nom from matieres m, specialite s where m.specialite=s.code''')
	data = cursor.fetchall()
	return render_template("consultermatiere.html",userDetails=data)
	

	
#----------------- Supprission d'une matiere ------------------------------	
@app.route("/supprimermatiere.html")
def supprimermatiere():
	return render_template("supprimermatiere.html",num=10)	
	
@app.route('/supprimermat',methods = ['POST', 'GET'])
def supprimermat():
	if request.method == 'POST':
		code = request.form['code']
		cursor = db.cursor()
		cursor.execute(''' delete from matieres where code=%s''',[code])
		db.commit()
		cursor.close()
		return f"Done!!"
	
	


#------------------- Page de gestion des spécialites -------------------	
@app.route("/specialite.html")
def spec():
	return render_template("specialite.html",num=10)

#------------------- Ajout d'une specialite ------------------------------
@app.route("/ajouterspecialite.html")
def ajouterspecialite():
	return render_template("ajouterspecialite.html",num=10)	
	
@app.route("/ajouterspec", methods = ['POST', 'GET'])
def ajouterspec():
	if request.method == 'POST':
        	code = request.form['code']
        	nom = request.form['nom']
        	niveau = request.form['niveau']
        	cursor = db.cursor()
        	cursor.execute(''' INSERT INTO specialite VALUES(%s,%s,%s)''',(code,nom,niveau))
        	db.commit()
        	cursor.close()
        	return render_template("res.html",msg="Spécialité ajouté avec succéesé")
        	
	
#------------------------- Modification d'une specialite --------------------	
@app.route("/modifierspecialite.html")
def modifierspecialite():
	cursor = db.cursor()
	cursor.execute('''SELECT * FROM specialite''')
	data = cursor.fetchall()
	cursor.close()
	return render_template("modifierspecialite.html",userDetails=data)	

@app.route("/modifierspec", methods = ['POST', 'GET'])
def modifierspec():
	if request.method == 'POST':
		code = request.form['nom']
		newname = request.form['newname']
		cursor = db.cursor()
		
		cursor.execute(''' UPDATE  specialite SET nom=%s where code=%s''',(newname,code))
		db.commit()
		cursor.close()
		return render_template("res.html",msg="Spécialité modifié avec succéesé")
	

				
#--------------- Supprission d'une specialite ----------------------------
@app.route("/supprimerspecialite.html")
def supprimerspecialite():
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM specialite''')
        data = cursor.fetchall()
        cursor.close()
        return render_template('supprimerspecialite.html',userDetails=data)

@app.route("/supprimerspec", methods = ['POST', 'GET'])
def supprimerspec():
	
	if request.method == 'POST':
        	
        	nom = request.form['nom']
        	
        	cursor = db.cursor()
        	
        	cursor.execute(''' delete from specialite where code=%s''',([nom]))
        	db.commit()
        	cursor.close()
        	return render_template("res.html",msg="specialite supprimé avec succées")	
 
#------------------- Consulter la liste des specialite -----------------------       	
@app.route("/consulterspecialite.html")
def consulterspecialite():
	cursor = db.cursor()
	cursor.execute(''' select * from specialite''')
	data = cursor.fetchall()
	cursor.close()		
	return render_template('consulterspecialite.html', userDetails=data)


#-------------------- Page de gestion des etudiants -------------------------	
@app.route("/etudiant.html")
def etudiant():
	return render_template("etudiant.html",num=10)	


#------------------- Ajouter un etudiant --------------------------------------	
@app.route("/ajouteretudiant.html")
def ajouteretudiant():
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM specialite''')
        data = cursor.fetchall()
        cursor.close()
        return render_template('ajouteretudiant.html',userDetails=data)
        
@app.route('/ajouteretud', methods = ['POST', 'GET'])
def ajouteretud():
   
    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        cin = request.form['cin']
        dns = request.form['dns']
        classe = request.form['classe']
        
        specialite = request.form['specialite']
        tel = request.form['tel']
        email = request.form['email']
        adresse = request.form['adresse']
        sexe = request.form['sexe']
        cursor = db.cursor()
        cursor.execute(''' INSERT INTO etudiant VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',(cin,nom,prenom,classe,dns,specialite,sexe,tel,email,adresse))
        db.commit()
        cursor.close()
        
        return "Done!"




#-------------------- Modifier un etudiant --------------------------------------	
@app.route("/modifieretudiant.html")
def modifieretudiant():
	return render_template("modifieretudiant.html",num=10)	

@app.route('/modifieretudiant.html/<cin>')
def modifieretudd(cin):
	cursor = db.cursor()
	cursor.execute(''' SELECT * FROM etudiant where cin=%s''',[cin])
	data = cursor.fetchone()
	cursor.execute(''' SELECT * FROM specialite''')
	datta=cursor.fetchall()
	cursor.close()
	return render_template('modifieretudiant.html',userDetails=data,idd=cin,spec=datta)


@app.route('/modifieretud/<idd>', methods = ['POST', 'GET'])
def modifieretud(idd):
	if request.method == 'POST':
		nom = request.form['nom']
		prenom = request.form['prenom']
		cin = request.form['cin']
		dns = request.form['dns']
		classe = request.form['classe']
		
		specialite = request.form['specialite']
		tel = request.form['tel']
		email = request.form['email']
		adresse = request.form['adresse']
		sexe = request.form['sexe']
		cursor = db.cursor()
		cursor.execute(''' UPDATE  etudiant SET cin=%s,nom=%s,prenom=%s,classe=%s,dns=%s,specialite=%s,sexe=%s,tel=%s,email=%s,adresse=%s where cin=%s''',(cin,nom,prenom,classe,dns,specialite,sexe,tel,email,adresse,[idd]))
		db.commit()
		cursor.close()
		return "Done"
	


#------------------ Supprimer une etudiant ----------------------------------
@app.route("/supprimeretudiant.html")
def supprimeretudiant():
	return render_template("supprimeretudiant.html",num=10)	
	
	
        
@app.route('/supprimeretud', methods = ['POST', 'GET'])
def supprimeretud():
   
    if request.method == 'POST':
        cin = request.form['cin']
        cursor = db.cursor()
        cursor.execute(''' DELETE FROM etudiant WHERE cin=%s''',[cin])
        db.commit()
        cursor.close()
        return "Done!"


#------------------------ Consulter la liste des etudiants -------------------------       
@app.route('/consulteretudiant.html')
def consulteretudiant():
        cursor = db.cursor()
        cursor.execute(''' SELECT * FROM specialite''')
        data=cursor.fetchall()
        cursor.close()
        return render_template('consulteretudiant.html',userDetails=data)
        

 
@app.route('/consulteretud', methods = ['POST', 'GET'])
def consulteretud():
	if request.method == 'POST':
		classe = request.form['classe']
		spec = request.form['specialite']
		cursor = db.cursor()
		cursor.execute(''' SELECT e.*, s.nom FROM etudiant e, specialite s where classe=%s and specialite=%s and e.specialite=s.code''',(classe,spec))
		data=cursor.fetchall()
		cursor.close()
		return render_template('user.html',userDetails=data)
       
@app.route('/user.html')
def user():
	return render_template('user.html')
       


#---------------- Page de gestion des notes -----------------------------------        	  
@app.route('/note.html')
def note():
	return render_template("note.html")
	
#---------------- Ajouter une note ---------------------------------------------

	
@app.route('/ajouternote.html')
def ajouternotee():
	cursor = db.cursor()
	cursor.execute(''' select * from specialite''')
	data = cursor.fetchall()
	cursor.close()
	return render_template('ajouternote.html',userDetails=data)  

@app.route('/notetudiant',methods = ['POST', 'GET'])
def notetudiant():

	if request.method == 'POST':
		classe = request.form['classe']
		sem = request.form['sem']
		specialite = request.form['specialite']
		cursor = db.cursor()
		
		cursor.execute(''' SELECT * FROM matieres where classe=%s  and specialite=%s and semestre=%s''',(classe,specialite,sem))
		data=cursor.fetchall()
		cursor.execute(''' SELECT * FROM specialite''')
		dataa=cursor.fetchall()
		cursor.close()
		return render_template('ajouternote.html',matDetails=data,userDetails=dataa,classe=classe,specialite=specialite)   
       
 
	
@app.route('/ajouternote/<spec>,<cl>',methods = ['POST', 'GET'])
def ajouternote(spec,cl):
	specialite=spec
	classe=cl
	if request.method == 'POST':
		mat = request.form['mat']
		cursor = db.cursor()
		cursor.execute('''select type from matieres where code=%s''',([mat]))
		data =  cursor.fetchone()
		if data[0] == "DsExaman" :
			return render_template("ajouter.html",specialite=spec,classe=cl,mat=mat)
		else:
			return render_template("ajouter2.html",specialite=spec,classe=cl,mat=mat)

#Ajouter une note  pour une matiere de type DsExaman
@app.route('/ajouter.html')
def ajouter(spec,cl,mt):
	return render_template("ajouter.html")
	

@app.route('/note/<cl>,<spec>,<mat>',methods = ['POST', 'GET'])
def ajout(cl,spec,mat):
	if request.method == 'POST':
		cin = request.form['cin']
		ds = request.form['ds']
		ex = request.form['ex']
		cursor = db.cursor()
		cursor.execute('''select * from etudiant where specialite=%s and classe=%s and cin=%s''',(spec,cl,cin))
		data =  cursor.fetchall()

		if data:
			msg = "note ajouté"
			moy= (float(ds)*0.3)+(float(ex)*0.7)
			cursor.execute(''' INSERT INTO note(cin,codeM,ds,ex,moy) VALUES(%s,%s,%s,%s,%s)''',(cin,mat,ds,ex,moy))
			db.commit()
				
		else:
			msg = "Aucun personne exite du cette identifiant à ce groupe"
		
		return render_template("res.html", msg=msg)


#Ajouter une note  pour une matiere de type TpDsExaman
@app.route('/ajouter2.html')
def ajouter2(spec,cl,mt):
	return render_template("ajouter2.html")


@app.route('/note2/<cl>,<spec>,<mat>',methods = ['POST', 'GET'])
def ajout2(cl,spec,mat):
	if request.method == 'POST':
		cin = request.form['cin']
		ds = request.form['ds']
		tp = request.form['tp']
		ex = request.form['ex']
		cursor = db.cursor()
		cursor.execute('''select * from etudiant where specialite=%s and classe=%s and cin=%s''',(spec,cl,cin))
		data =  cursor.fetchall()

		if data:
			msg = "note ajouté"
			moy= (float(tp)*0.1)+(float(ds)*0.2)+(float(ex)*0.7)
			cursor.execute(''' INSERT INTO note(cin,codeM,tp,ds,ex,moy) VALUES(%s,%s,%s,%s,%s,%s)''',(cin,mat,tp,ds,ex,moy))
			db.commit()
				
		else:
			msg = "Aucun personne exite du cette identifiant à ce groupe"
		
		return render_template("res.html", msg=msg)

	
		
#------------------ Modifier une note ----------------------------------------         
@app.route('/modifiernote.html')
def modifiernotee():
	return render_template("modifiernote.html")
	
#Verification de l'existance du code de matiere entrée    	
@app.route('/modnote', methods =['POST','GET'])
def modnote():
	if request.method == 'POST':
		cin = request.form['cin']
		code = request.form['code']
		cursor = db.cursor()
		cursor.execute('''select * from matieres where code=%s''',([code]))
		data = cursor.fetchone()
		if data: 
			if data[5] == 'DsExaman':
	
				return render_template("modifiernote1.html",cin=cin,data=data)
			else:
				return render_template("modifiernote2.html",cin=cin,data=data)
		else:
		 	return("matiere erronée")


#Modifier une note pour une matiere de type DsExaman
@app.route('/modifiernote1.html')
def modifiernote1():
	return render_template("modifiernote1.html")
	
	
@app.route('/modnote1/<cin>,<code>',methods = ['POST', 'GET'])
def modnote1(cin,code):
	if request.method == 'POST':
		ds = request.form['ds']
		ex = request.form['ex']
		cursor = db.cursor()
		cursor.execute('''select * from etudiant where cin=%s''',([cin]))
		data =  cursor.fetchall()
		

		if data:
			msg = "note modifié"
			
			cursor.execute(''' UPDATE  note SET ds=%s and ex=%s where cin=%s and codem=%s ''',(ds,ex,[cin],[code]))
			db.commit()
			moy= (float(ds)*float(0.3))+(float(ex)*float(0.7))
			cursor.execute(''' UPDATE  note SET  moy=%s where cin=%s and codem=%s''',(moy,[cin],[code]))
			db.commit()	
		else:
			msg = "Aucun personne exite du cette identifiant à ce groupe"
		
		return render_template("res.html", msg=msg)
		


@app.route('/modifiernote2.html')
def modnotee2():
	return render_template("modifiernote2.html")             
#Modifier une note pour une matiere de type TpDsExaman
@app.route('/modnote2/<cin>,<code>',methods = ['POST', 'GET'])
def modnote2(cin,code):
	if request.method == 'POST':
		ds = request.form['ds']
		tp = request.form['tp']
		ex = request.form['ex']
		cursor = db.cursor()
		cursor.execute('''select * from etudiant where cin=%s''',[cin])
		data =  cursor.fetchone()

		if data:
			msg = "note modifié"
			moy= (float(tp)*0.1)+(float(ds)*0.2)+(float(ex)*0.7)
			cursor.execute(''' UPDATE  note SET tp=%s and ds=%s and ex=%s and moy=%s where cin=%s and codem=%s''',(tp,ds,ex,moy,[cin],[code]))
			db.commit()
				
		else:
			msg = "Aucun personne existe du cette identifiant"
		
		return render_template("res.html", msg=msg)




#------------------------ Supprimer une note -------------------------------------	
@app.route('/supprimernote.html')
def supprimernote():
	return render_template("supprimernote.html")
	
@app.route('/supprimernote', methods =['POST','GET'])	
def supnote():
	if request.method == 'POST':
		cin = request.form['cin']
		code = request.form['code']
		cursor = db.cursor()
		cursor.execute('''delete from note where cin=%s and codem=%s''',(cin,code))
		db.commit()
		msg = " Note supprimé avec succées" 
		return render_template("res.html",msg=msg)
		

#--------------------- Consulter le bultin de l'étudiant ----------------------
@app.route('/consulternote.html')
def consulternote():
	return render_template("consulternote.html")
@app.route('/consultnote', methods =['POST','GET'])
def consultnote():
	if request.method == 'POST':
		cin = request.form['cin']
		cursor = db.cursor()
		cursor.execute('''select e.*, s.nom from  etudiant e, specialite s where e.specialite=s.code and cin=%s''',([cin]))
		data =  cursor.fetchone()
		cursor.execute('''select code, nom ,type from  matieres where  specialite=%s and classe=%s''',(data[5],data[3]))
		mat = cursor.fetchall()
		cursor.execute('''select * from  note where  cin=%s''',[cin])
		note =  cursor.fetchall()
		#cursor.execute('''select * from  specialite where  code=%s''',(data[6]))
		#spec =  cursor.fetchone()
		return render_template('affichage.html',data=data,mat=mat,note=note)
		
		
		
		
		
	
#-------------- Page d'affichage des messages ---------------------------------------
@app.route('/res.html')
def res():
	return render_template("res.html")	

	



if __name__=="__main__":
	app.run(host='0.0.0.0', port=5000)

