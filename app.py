from flask import Flask, request, render_template

app = Flask(_name_)

class Medicine:
    def _init_(self, Tablet, Brand, Compositions, SideEffects, Purpose, Cost):
        self.Tablet = Tablet
        self.Brand = Brand
        self.Compositions = Compositions
        self.SideEffects = SideEffects
        self.Purpose = Purpose
        self.Cost = Cost

    def _str_(self):
        return (f"Tablet: {self.Tablet}\n"
                f"Brand: {self.Brand}\n"
                f"Compositions: {', '.join(self.Compositions)}\n"
                f"SideEffects: {', '.join(self.SideEffects)}\n"
                f"Purpose: {self.Purpose}\n"
                f"Cost: {self.Cost}\n")


def find_similar_medicines(tablet_name, medicines_list):
    input_medicine = None
    for medicine in medicines_list:
        if medicine.Tablet.lower() == tablet_name.lower():
            input_medicine = medicine
            break

    if not input_medicine:
        return f"No medicine found with the name {tablet_name}", []

    similar_medicines = []
    for medicine in medicines_list:
        if medicine.Tablet.lower() != input_medicine.Tablet.lower():
            if set(medicine.Compositions) & set(input_medicine.Compositions):  # Check for any common composition
                similar_medicines.append(medicine)

    return input_medicine, similar_medicines


predefined_medicines = [
        Medicine("Zyloric","Glaxo SmithKline Pharmaceuticals " ,["Allopurinol"] , ["Diarrhea" ," Nausea"] ," Gout" , " 10 for 63/-"),
        Medicine("Logout"," Inga Laboratories" , ["Allopurinol"] , ["Diarrhea","Nausea"] ,"Gout " , "10 for 104/- "),
        Medicine("Amoxible","Zeelab Pharmacy", ["Amoxycillin"],["Nausea","Diarrhea","Skin rash","Vomitting"],"	Fever","10 for 25/-"),
        Medicine("MEF+","Zeelab Pharmacy",["Mefanamic acid","paracetamol"],["Nausea","Vomitting",",Diarrhea","Indigestion","Heartburn"],"Fever","10 for 23/-"),
        Medicine("Logout"," Inga Laboratories" , ["Allopurinol"] , ["Diarrhea" ,"Nausea "] ,"Gout " , "10 for 104/- "),
        Medicine("Ciploric"," Cipla" ,["Allopurinol"], ["Diarrhea" ,"Nausea "] ," Gout" , " 10 for 19/-"),
        Medicine("Tilistigmin","Tablets India Ltd ",["Neostigmine"], [" Nausea" ,"Vomitting ",",Abdominal cramp","Diarrhea"] ,"Muscle relaxation " , "10 for 50/- "),
        Medicine("Bizlo"," Torrent Pharmaceuticals",["Baclofen"], ["Nausea","Constipation","Headache","Sedation","Chills","Dizziness","Convulsion"] ," Muscle relaxation" , "10 for 124/- "),
        Medicine("Spinobak","Mankind Pharmaceuticals ",["Baclofen"], ["Dizziness","Convulsion","Nausea","Headache","Sedation","Chills","Constipation"] ,"Muscle relaxation " , "10 for 95/- "),
        Medicine("Lioresal 26"," Novartis India Ltd",["Baclofen"], ["Dizziness","Convulsion","Nausea","Headache","Sedation","Chills","Constipation"] ," Muscle relaxation" , "10 for 453/- "),
        Medicine("Baclof 26","Intas Pharmaceuticals ",["Baclofen"], [ "Dizziness","Convulsion","Nausea","Headache","Sedation","Chills","Constipation"] ," Muscle relaxation" , " 10 for 366/-"),
        Medicine("Powergesic MR ","Jenburkt Pharmaceuticals " , ["Chlorozoxazone","Diclofenac","Paracetmol"] , ["Nausea","Vomitting","Heartburn","Diarrhea","Dryness "] ,"Inflammation " , "10 for 199/- "),
        Medicine("Mobizox"," Sun Pharmaceutical Industries Ltd" , ["Chlorozoxazone","Diclofenac","Paracetmol"] , ["Nausea","Vomitting","Heartburn","Diarrhea","Stomach pain"] ,"Inflammation" , "10 for 258/- "),
        Medicine("Zeedonac-MR Novo"," Alkem Laboratories" , ["Chlorozoxazone","Diclofenac","Paracetmol"] , ["Nausea","Vomitting","Heartburn","Diarrhea","Stomach pain"] ,"Inflammation " , "10 for 75/- "),
        Medicine("Dicomol"," Zeelab Pharmaceuticals" , ["Chlorozoxazone","Diclofenac","Paracetmol"] , ["Heartburn","Nausea","Dryness","Vomitting "] ," Inflammation" , " 10 for 22/-"),
        Medicine("Chymothal Forte","Cadila Pharmaceuticals " , ["Trypsin Chymotrypsin"] , ["Bloating","Rashes","Indigestion"] ,"Inflammation" , "20 for 416/- "),
        Medicine("Enzoflam-CT","Alkem Laboratories " , ["Trypsin Chymotrypsin  "] , ["Bloating","Rashes","Indigestion"] ,"Inflammation " , " 15 for 299/-"),
        Medicine("Chymocip","Cipla " , ["Trypsin Chymotrypsin" ] , ["Bloating","Rashes","Indigestion"] ,"Inflammation " , " 20 for 441/-"),
        Medicine("Chymoral Forte","Torrent Pharmaceuticals Ltd " , ["Trypsin Chymotrypsin "] , ["Rashes"] ," Inflammation" , " 20 for 476/-"),
        Medicine("Rixmin","Cipla" , ["Rifaximin"] , ["Dizziness","Nausea","Fatigue","Depression","Rash"] ,"Diarrhea" , "10 for 420/- "),
        Medicine("Lomo","Shridhara Lifescienes " , ["Loperamide "] , ["Nausea","Constipation","Headache","Stomach pain"] ,"Diarrhea " , "10 for 20/- "),
        Medicine("Rifaxin","ANT Pharma Pvt Ltd " , ["Rifaximin"] , ["Dizziness","Nausea","Fatigue","Depression","Rash"] ,"Diarrhea " , "10 for 390/- "),
        Medicine("Ridol","Gufic Bioscience Ltd " , ["Loperamide  "] , ["Nausea","Constipation","Headache","Stomach pain "] ,"Diarrhea " , "10 for 25/- "),
        Medicine("Lopamide","Torrent Pharma Ltd " , ["Loperamide  "] , ["Constipation","Headache","Nausea","Stomach pain"] ,"Diarrhea " , "10 for 25/- "),
        Medicine("Rifaset","Macleods Pharma Pvt Ltd " , ["Rifaximin"] , ["Dizziness","Nausea","Fatigue","Pains","Rashes"] ,"Diarrhea " , "10 for 381/- "),
        Medicine("Pansec","Cipla " , ["Pantaprazole"] , ["Diarrhea","Flatulence","Headache","Vomitting","Nausea","Dizziness "] ,"Ulcers " , "15 for 217/- "),
        Medicine("Pantin","Hetero Drugs " , ["Pantaprazole"] , ["Diarrhea","Flatulence","Headache","Vomitting","Nausea","Dizziness "] ,"Ulcers " , "15 for 111/- "),
        Medicine("Zypan","Apa Pharmaceuticals " , ["Pantaprazole"] , ["Diarrhea","Flatulence","Headache","Vomitting","Nausea","Dizziness "] ,"Ulcers " , "10 for 69/- "),
        Medicine("Pantop","Aristo Pharmaceuticals" , ["Pantaprazole"] , ["Diarrhea","Flatulence","Headache","Vomitting","Nausea","Dizziness "] ,"Ulcers " , "15 for 165/- "),
        Medicine("Dolo 650","Microlabs " , ["Acetaminophin","Paracetmol"] , ["Stomach pain" ,"Nausea","Vomitting"] ," Fever" , "15 for 34/-"),
        Medicine("Paracip","Cipla Ltd " , ["Acetaminophin","Paracetmol"] , ["Stomach pain" ,"Nausea","Vomitting"] ," Fever" , "10 for 10/-"),
        Medicine("Race","Rhombus Pharmaceuticals " , ["Aceclofenac "] , ["Stomach pain" ,"Nausea ","Vomitting","Indigestion","Diarrhea"] ,"Pain relief " , "10 for 40/- "),
        Medicine("Amtoril","Macleads Pharmaceuticals " ,  ["Tolmeting "] ,["Stomach pain" ,"Nausea ","Vomitting","Indigestion"]," Pain relief" , "10 for 40/-  "),
        Medicine("Indamol","Indamed Pharmaceuticals " , ["Aceclofenac ","Paracetmol "] ,["Stomach pain" ,"Nausea ","Vomitting","Indigestion"]," Pain relief" , "10 for 28/-  "),
        Medicine("Cemol","Inga Laboratories " , ["Acetaminophen ","Paracetmol "] , ["Stomach pain" ,"Nausea ","Vomitting",] ,"Pain relief " , "10 for 5/- "),
        Medicine("Oropyrin","Ortin Laboratories " , ["Acetaminophen ","Paracetmol "] , ["Stomach pain" ,"Nausea ","Vomitting",] ,"Pain relief " , "10 for 15/- "),
        Medicine("Pimol","Pioneer pharmaceuticals " , ["Acetaminophen ","Paracetmol "] , ["Stomach pain" ,"Nausea ","Vomitting",] ,"Pain relief " , "10 for 15/- "),
        Medicine("Ketorol-DT","Dr Reddys Laboratories " , ["Ketorolac "] , ["Vomitting" ,"Indigestion ","Diarrhea","Nausea","Heartburn"] ,"Pain relief " , "15 for 162/- "),
        Medicine("Cipflam","Cipla Ltd " , ["Ibuprofen ","Paracetmol  "] , ["Heartburn","Nausea","Indigestion","Stomach pain" ] ,"Pain relief " , "15 for 12/-"),
        Medicine("Naprosyn","RPG Life Sciences " ,  ["Naproxen "] , ["Indigestion","Nausea","Headache","Rash","Bruise","Edema"] ,"Pain relief " , "10 for 95/-"),
        Medicine("Relief","Laborate Pharmaceuticals " , ["Ibuprofen ","Paracetmol  "] , ["Heartburn","Indigestion","Nausea","Stomach pain"] ,"Pain relief  " , "10 for 95/- "),
        Medicine("Omez"," Dr Reddys Laboratories" , ["Omeprazole "], ["Diarrhea","Flatulence","Headache","Nausea","Vomitting"] ,"Indigestion " , "20 for 64/- "),
        Medicine("Famocid","Sun Pharmaceuticals " ,  ["Famotidine "],  ["Headache","Dizziness","Diarrhea","Constipation"] ,"Indigestion " , "20 for 64/- "),
        Medicine("Topcid","Torrent pharmaceuticals " , ["Famotidine "] , ["Headache","Dizziness","Diarrhea","Constipation"] ,"Indigestion " , "14 for 9/- "),
        Medicine("Suziran","Suzikem drugs " ,  ["Ranitidine "] , ["Headache" ,"Diarrhea "] ,"Indigestion " , "10 for 23/- "),
        Medicine("Bisotidine ","Globela Pharmaceuticals" ,  ["Cimetidine "] , ["Headache","Dizziness","Diarrhea","Muscle pain","Rashes"] ,"Indigestion " , "10 for 29/-"),
        Medicine("Tymidin","Abott " ,  ["Cimetidine "] , ["Headache","Dizziness","Diarrhea","Muscle pain","Rashes"] ,"Indigestion " , "10 for 8/-"),
        Medicine("Famoflan","Ethix healthcare " , ["Famotidine"], ["Headache","Diarrhea","Dizziness","Constipation"] ," Indigestion" , "10 for 10/- "),
        Medicine("Mega"," Embiotic laboratories" , ["Magaldrate ","Simethicone "] , ["Chalky taste","Diarrhea","Constipation"] ,"Indigestion " , "8 for 7/- "),
        Medicine("Zingaro","Adco ltd " ,["Magaldrate ","Simethicone "] , ["Chalky taste","Diarrhea","Constipation"] ,"Indigestion " , "8 for 7/- "),
        Medicine("Axid","Apex laboratories " ,  ["Nizatidine "] , ["Fatigue","Drowsiness","Headache","Constipation"] ,"Indigestion " , " 10 for 41/-"),
        Medicine("Gerd","Spectracare Laboratories " ,  ["Pantaprazole	 "] , ["Diarrhea","Flatulence","Headache","Nausea","Stomach pain","Dizziness"] ,"Indigestion " , "10 for 60/-"),
        Medicine("Bloateez","Cogentrix Pharmaceuticals " ,  ["Alpha Galactosidase"] , ["Nausea","Diarrhea","Vomitting"] ,"Indigestion " , " 10 for 65/-"),
        Medicine("Oskar","Mankind Pharmaceuticals " , ["Omaprazole  "] , ["Diarrhea","Fatulence","Headache","Nausea","Vomitting","Abdominal pain "] ,"Ulcers " , "10 for 32/- "),
        Medicine("Ome ppi","Blue Cross Laboratories " , ["Omaprazole "] , ["Diarrhea","Fatulence","Headache","Nausea","Vomitting","Abdominal pain "] ,"Ulcers " , "10 for 27/- "),
        Medicine("Omez","Dr Reddys Laboratories " , ["Omaprazole "] , ["Diarrhea","Fatulence","Headache","Nausea","Vomitting","Abdominal pain "] ,"Ulcers " , "20 for 64/- "),
        Medicine("Lanzopen","Morepen Laboratories " , ["Lansoprazole "] , ["Nausea","Headache","Flatulence","Diarrhea"] ,"Ulcers " , "10 for 25/- "),
        Medicine("Locide","Psychotropics India Ltd " , ["Lansoprazole"] ,["Nausea","Headache","Flatulence","Diarrhea"] ,"Ulcers " , "10 for 80/- "),
        Medicine("Lanzol","Cipla " , ["Lansoprazole "] , ["Nausea","Headache","Flatulence","Diarrhea"]  ,"Ulcers " , "10 for 99/- "),
        Medicine("Prevacid","Edinburg Pharmaceuticals " , ["Pantaprazole "] , ["Diarrhea","Flatulence","Headache","Nausea","Vomitting","Dizziness"] ,"Indigestion " , " 10 for 57/-"),
        Medicine("Anti cold","Safe Life Care " , [ " Paracetmol","Caffiene","Phenylephrine","Diphenydramine "] , ["Nausea","Vomitting","Insomnia","Headache","Tremors"] ,"Cold " , " 10 for 70/-"),
        Medicine("Cheston cold","Cipla " , ["Cetirizine","Paracetmol","Phenylephrine  "] , ["Nausea","Vomitting","Headache","Fatigue","Dizziness","Dryness"] ," Cold" , "10 for 47/- "),
        Medicine("Okacet cold"," Cipla" ,  ["Cetirizine","Paracetmol","Phenylephrine  "] , ["Nausea","Vomitting","Headache","Fatigue","Dizziness","Dryness"] ," Cold" , "10 for 51/- "),
        Medicine("Cetzine","Dr Reddys Laboratories " , ["Cetirizine "] , ["Dryness","Headache","Constipation","Sleepiness","Fatigue","Vomitting"] ," Cold" , "15 for 32/- "),
        Medicine("Accpar P","Gracica Life Science India Pvt Ltd " , ["Aceclofenac ","Paracetmol "] , ["Nausea","Vomitting","Stomach pain","Heartburn","Loss of appetite "] ,"Cold " , "15 for 32/- "),
        Medicine("Crocin","Glaxo Smithkline Pharmaceuticals " , [ "Acetaminophen "," Paracetmol "] , ["Stomach pain" ,"Nausea ","Vomitting"] ,"Cold " , "20 for 20/- "),
        Medicine("Nasorest","Zydus Cadila " , ["Caffeine","Paracetmol","Phenylephrine","Acrivastine"] , ["Nausea","Headache","Vomitting","Restlessness","Sleepiness"] ," Cold" , " 10 for 40/-"),
        Medicine("Dexodil","Psychotropics India Ltd " , ["Dexchlorpheniramine "] , ["Sleepiness "] ,"Cold " , "10 for 63/- "),
        Medicine("Cofmont","Euronova Pharmaceuticals " , ["Levocetirizine","Montelukast  "] , ["Nausea","Diarrhea","Dryness","Fatigue","Headache","Sleepiness"] ,"	Cold " , " 	10 for 118/-"),
        Medicine("Coldrex","Astonia Labs Pvt Ltd " , ["Aceclofenac","Phenylephrine","Paracetmol","Cetirizine","Caffiene"] , ["Nausea","Vomitting","Stomach pain","Restlessness","Heartburn"] ," Cold" ,"10 for 44/-"),
]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        tablet_name = request.form["tablet_name"]
        input_medicine, similar_medicines = find_similar_medicines(tablet_name, predefined_medicines)
        if isinstance(input_medicine, str):
            return render_template("result.html", message=input_medicine)
        else:
            return render_template("result.html", input_medicine=input_medicine, similar_medicines=similar_medicines)
    return render_template("result.html")

if _name_ == "_main_":
    app.run(debug=True)
