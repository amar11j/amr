import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image


with st.sidebar:
    Pilihan= option_menu('Healthy Weagy',['Laki-Laki','Perempuan','Kalori Makanan','Aktivitas','Program','Feedback'],icons=['gender-male','gender-female','basket2','activity','clipboard2-pulse','clipboard2-pulse'],default_index=0)

#Laki-laki                         
if(Pilihan=='Laki-Laki'):
    st.title('Hitung Indeks Massa Tubuh') 
    berat= st.number_input("Berat Badan(Kg)",0)
    tinggi= st.number_input("Tinggi Badan(cm)",0)
    umur=st.number_input("Umur(Tahun)",0)
    hitung=st.button("Hitung")
    if hitung:
        IMT=berat/((tinggi/100)*(tinggi/100))
        st.success(f"IMT anda adalah= {IMT}")
        if(IMT<18.5):
            #st.write("Anda termasuk dalam golongan tubuh Kurus")
            st.success("Anda termasuk dalam golongan tubuh Kurus")
        if(18.5<=IMT<=22.9):
            st.success("Anda termasuk dalam golongan tubuh Normal")
        if(23<=IMT<=27.5):
            st.success("Anda termasuk dalam kelebihan berat badan")
        if(IMT>27.5):
            st.success("Bisa yuk Diet")
        
    st.title('Kebutuhan Kalori Harian')
    hitung2=st.button("Hitung Kalori")
    if hitung2:
        rumus=(66.5+(13.75*berat)+(5.003*tinggi)-(6.75*umur))*1.2
        st.success(f"Jumlah kalori harian Anda adalah={rumus} kkal")
        
#Perempuan
if(Pilihan=='Perempuan'):
    st.title('Hitung Indeks Massa Tubuh')                         
    berat= st.number_input("Berat Badan(Kg)",0)
    tinggi= st.number_input("Tinggi Badan(cm)",0)
    umur=st.number_input("Umur(Tahun)",0)
    hitung=st.button("Hitung")
    if hitung:
        IMT=berat/((tinggi/100)*(tinggi/100))
        #st.write("IMT anda adalah =",IMT)
        st.success(f"IMT Anda adalah= {IMT}")
        if(IMT<18.5):
            #st.write("Anda termasuk dalam golongan tubuh Kurus")
            st.success("Anda termasuk dalam golongan tubuh Kurus")
        if(18.5<=IMT<=22.9):
            st.success("Anda termasuk dalam golongan tubuh Normal")
        if(23<=IMT<=27.5):
            st.success("Anda termasuk dalam golongan tubuh Overweight")
        if(IMT>27.5):
            st.success("Anda termasuk dalam golongan tubuh Obesitas")
        
    st.title('Kebutuhan Kalori Harian')
    hitung2=st.button("Hitung Kalori")
    if hitung2:
        rumus2=(655.1+(9.563*berat)+(1.850*tinggi)-(4.676*umur))*1.2
        st.success(f"Jumlah kalori harian Anda adalah= {rumus2} kkal")

#Kalori Makanan
if(Pilihan=='Kalori Makanan'):
    st.title('Hitung Kalori Makanan Anda')
    nasi= st.number_input("Nasi(gr)")
    ayam= st.number_input("Ayam(gr)")
    telur= st.number_input("Telur(gr)")
    tempe= st.number_input("Tempe(gr)")
    tahu= st.number_input("Tahu(gr)")
    sayur= st.number_input("sayur(gr)")
    daging= st.number_input("Daging(gr)")
    hitung3=st.button("Hitung")
    if hitung3:
        kalori=1.3*nasi+(2.39*ayam)+(1.55*telur)+(0.652*sayur)+(1.93*tempe)+(0.76*tahu)+(1.434*daging)
        st.success(f"Kalori makanan Anda adalah= {kalori} kkal")


#Olahraga
if(Pilihan=='Aktivitas'):
    st.title('Pilih Aktivitas')
    check=st.checkbox("Duduk di Kursi")
    check1=st.checkbox("Berjalan")
    check2=st.checkbox("Bersepeda")
    check3=st.checkbox("Berlari")
    check4=st.checkbox("Membawa belanjaan menaiki tangga")
    check5=st.checkbox("Lompat tali")
    check6=st.checkbox("Menaiki tangga dengan langkah cepat")
    check7=st.checkbox("Menyapu lantai")
    check8=st.checkbox("Mencuci piring")
    st.title('Masukkan Data Anda')
    durasi= st.number_input("Durasi(menit)")
    beratbadan= st.number_input("Berat Badan(Kg)")
    but=st.button("Cek kalori yang terbakar")
    if check:
        if but:
            rumus4=durasi*(1.3*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus4} kal")
    if check1:
        if but:
            rumus5=durasi*(2*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus5} kal")
    if check2:
        if but:
            rumus6=durasi*(3.5*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus6} kal")
    if check3:
        if but:
            rumus7=durasi*(8.3*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus7} kal")
    if check4:
        if but:
            rumus8=durasi*(7.5*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus8} kal")
    if check5:
        if but:
            rumus9=durasi*(12.3*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus9} kal")
    if check6:
        if but:
            rumus10=durasi*(8.8*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus10} kal")
    if check7:
        if but:
            rumus11=durasi*(3.5*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus11} kal")
    if check8:
        if but:
            rumus12=durasi*(2.2*3.5*beratbadan)/200
            st.success(f"Kalori yang terbakar adalah = {rumus12} kal")

#Program
if(Pilihan=='Program'):
    st.title('Masukkan Data Anda')
    beratbdn=st.number_input("Berat Badan(Kg)",0)
    tinggibdn=st.number_input("Tinggi Badan(cm)",0)
    usia=st.number_input("Umur(Tahun)",0)
    check5=st.checkbox("Laki-Laki")
    check6=st.checkbox("Perempuan")
    st.title('Pilih Program yang mau diikuti')
    but1=st.button("Defisit Kalori")
    but2=st.button("Surplus Kalori")
    if but1:
        if check5:
            defisitkal=((10*beratbdn)+(6.25*tinggibdn)-(5*usia)+5)*1.2
            st.success(f"Kalori yang anda butuhkan untuk defisit kalori adalah = {defisitkal} kkal")
            #Karbo
            st.subheader('Rekomendasi Sumber Karbohidrat')
            karbohidrat=((60/100)*defisitkal)/4
            st.success(f"Karbohidrat yang anda harus konsumsi dalam sehari adalah = {karbohidrat} gr")
            st.write("Rekomendasi karbohidrat yang bisa dikonsumsi untuk defisit kalori adalah oatmeal,kentang,nasi merah, dan kacang-kacangan, ubi jalar. Dibawah ini adalah kandungan karbohidrat dari makanan tersebut:")
            image = Image.open('1.png')
            st.image(image, caption='Sumber Karbohidrat by Amar Intifada')
            #protein
            st.subheader('Rekomendasi Sumber Protein')
            protein=((15/100)*defisitkal)/4
            st.success(f"Protein yang harus anda konsumsi dalam sehari adalah = {protein} gr.")
            st.write("Rekomendasi protein untuk defisit kalori adalah dada ayam, daging tanpa lemak, susu whey protein,kedelai(edamame),kacang-kacangan,telur. Berikut adalah kandungan protein dari bahan makanan tersebut: ")
            image = Image.open('2.png')
            st.image(image, caption='Sumber Protein by Amar Intifada')
            #lemak
            st.subheader('Rekomendasi Sumber Lemak')
            lemak=((15/100)*defisitkal)/9
            st.success(f"Lemak yang anda butuhkan adalah = {lemak} gr.")
            st.write("Rekomendasi lemak sehat yang bisa dikonsumsi adalah alpukat, ikan,keju ,telur, tempe. Berikut adalah kandungan lemak dari bahan makanan tersebut.")
            image = Image.open('3.png')
            st.image(image, caption='Sumber Lemak by Amar Intifada')
            
        if check6:
            defisitkalo=((10*beratbdn)+(6.25*tinggibdn)-(5*usia)-161)*1.2
            st.success(f"Kalori yang anda butuhkan untuk defisit kalori adalah = {defisitkalo} kkal")
            #karbo
            st.subheader('Rekomendasi Sumber Karbohidrat')
            karbohidrat=((60/100)*defisitkalo)/4
            st.success(f"Karbohidrat yang anda harus konsumsi dalam sehari adalah = {karbohidrat} gr")
            st.write("Rekomendasi karbohidrat yang bisa dikonsumsi untuk defisit kalori adalah oatmeal,kentang,nasi merah, dan kacang-kacangan, ubi jalar. Dibawah ini adalah kandungan karbohidrat dari makanan tersebut:")
            image = Image.open('1.png')
            st.image(image, caption='Sumber Karbohidrat by Amar Intifada')
            #protein
            st.subheader('Rekomendasi Sumber Protein')
            protein=((15/100)*defisitkalo)/4
            st.success(f"Protein yang anda harus konsumsi dalam sehari adalah = {protein} gr")
            st.write("Rekomendasi protein untuk defisit kalori adalah dada ayam, daging tanpa lemak, susu whey protein,kedelai(edamame),kacang-kacangan,telur. Berikut adalah kandungan protein dari bahan makanan tersebut: ")
            image = Image.open('2.png')
            st.image(image, caption='Sumber Protein by Amar Intifada')
            #lemak
            st.subheader('Rekomendasi Sumber Lemak')
            lemak=((15/100)*defisitkalo)/9
            st.success(f"Lemak yang harus anda konsumsi dalam sehari adalah = {lemak} gr")
            st.write("Rekomendasi lemak sehat yang bisa dikonsumsi adalah alpukat, ikan,keju ,telur, tempe. Berikut adalah kandungan lemak dari bahan makanan tersebut.")
            image = Image.open('3.png')
            st.image(image, caption='Sumber Lemak by Amar Intifada')
            
    if but2:
        if check5:
            rumus=((66.5+(13.75*beratbdn)+(5.003*tinggibdn)-(6.75*usia))*1.2)+500
            st.success(f"Kalori yang dibuthkan untuk surpluss kalori adalah ={rumus}kkal")
            #Karbo
            karbohidrat=((60/100)*rumus)/4
            st.subheader('Rekomendasi Sumber Karbohidrat')
            st.success(f"Karbohidrat yang anda harus konsumsi dalam sehari adalah = {karbohidrat} gr")
            st.write("Rekomendasi karbohidrat untuk surplus kalori adalah nasi, kentang, roti gandum, pasta, singkong. Berikut adalah kandungan karbohidrat dari bahan makanan tersebut:")
            image = Image.open('4.png')
            st.image(image, caption='Sumber Karbohidrat by Amar Intifada')
            #Protein
            st.subheader('Rekomendasi Sumber Protein')
            protein=((15/100)*rumus)/4
            st.success(f"Protein yang anda harus konsumsi dalam sehari adalah = {protein} gr.")
            st.write("Rekomendasi protein untuk surplus kalori adalah daging merah, telur, ikan salmon,dada ayam, susu gainmass atau penambah berat badan,telur,tempe. Berikut adalah kandungan protein dari bahan makanan tersebut:")
            image = Image.open('5.png')
            st.image(image, caption='Sumber Protein by Amar Intifada')
            #Lemak
            st.subheader('Rekomendasi Sumber Lemak')
            lemak=((25/100)*rumus)/9
            st.success(f"Lemak yang anda harus konsumsi dalam sehari adalah = {lemak} gr")
            st.write(" Rekomendasi lemak yang bisa dikonsumsi untuk surplus kalori adalah selai kacang, keju, ikan salmon, coklat. Berikut adalah kandungan lemak dari bahan makanan tersebut:")
            image = Image.open('6.png')
            st.image(image, caption='Sumber Lemak by Amar Intifada')
            
        if check6:
            rumus2=((655.1+(9.563*beratbdn)+(1.850*tinggibdn)-(4.676*usia))*1.2)+400
            st.success(f"Kalori yang dibuthkan untuk surpluss kalori adalah ={rumus2}kkal")
            #Karbo
            st.subheader('Rekomendasi Sumber Karbohidrat')
            karbohidrat=((60/100)*rumus2)/4
            st.success(f"Karbohidrat yang anda harus konsumsi dalam sehari adalah = {karbohidrat} gr")
            st.write("Rekomendasi karbohidrat untuk surplus kalori adalah nasi, kentang, roti gandum, pasta, singkong. Berikut adalah kandungan karbohidrat dari bahan makanan tersebut:")
            image = Image.open('4.png')
            st.image(image, caption='Sumber Karbohidrat by Amar Intifada')
            #Protein
            st.subheader('Rekomendasi Sumber Protein')
            protein=((15/100)*rumus2)/4
            st.success(f"Protein yang anda harus konsumsi dalam sehari adalah = {protein} gr.")
            st.write("Rekomendasi protein untuk surplus kalori adalah daging merah, telur, ikan salmon,dada ayam, susu gainmass atau penambah berat badan,telur,tempe. Berikut adalah kandungan protein dari bahan makanan tersebut:")
            image = Image.open('5.png')
            st.image(image, caption='Sumber Protein by Amar Intifada')
            #Lemak
            st.subheader('Rekomendasi Sumber Lemak')
            lemak=((25/100)*rumus2)/9
            st.success(f"Lemak yang anda harus konsumsi dalam sehari adalah = {lemak} gr")
            st.write(" Rekomendasi lemak yang bisa dikonsumsi untuk surplus kalori adalah selai kacang, keju, ikan salmon, coklat. Berikut adalah kandungan lemak dari bahan makanan tersebut:")
            image = Image.open('6.png')
            st.image(image, caption='Sumber Lemak by Amar Intifada')
            
if(Pilihan=='Feedback'):
    st.success(f"https://forms.gle/HDPMFF9rfATvoEta7")
    


    
            
        
