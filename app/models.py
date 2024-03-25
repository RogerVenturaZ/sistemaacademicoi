from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Cidade")
    uf = models.charfiel(max_length=2, verbose_name="UF")
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        
class AreaSaber(models.Model): 
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Area")   
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = "AreaSaber"
        verbose_name_plural = "AreaSaberes"
        
class Instituicao (models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Instituição") 
    site = models.CharField(max_length = 100 , verbose_name = "Nome do Site ")   
    telefone = models.CharField(max_length = 100, verbose_name = "N° de Telefone") 
    cidade =  models.ForeignKey (Cidade, on_delete = models.CASCADE,verbose_name = "Nome da Cidade da Instituição")  
    def __str__(self) :
        return f"{self.nome},{self.site},{self.telefone},{self.cidade}"
    class Meta:
        verbose_name = "Instituicao"
        verbose_name_plural = "Instituicoes"

class Curso (models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome do Curso")     
    carga_horaria_total = models.CharField(max_lenght = 100 , verbose_name = "N° de Horas no Total")  
    duracao_meses =  models.CharField(max_lenght = 100 , verbose_name = "N° de meses") 
    areasaber = models.ForeignKey(AreaSaber, on_delete = models.CASCADE,verbose_name = "Nome da Area")
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE, verbose_name = "Nome da Instituicao")
    def __str__ (self):
        return f"{self.nome},{self.carga_horaria_total},{self.duracao_meses},{self.areasaber},{self.instituicao}"
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        
class Disciplina(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Disciplina")  
    areasaber = models.ForeignKey(AreaSaber, on_delete = models.CASCADE,verbose_name = "Nome da Area")      
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE, verbose_name = "Nome do Curso" )
    def __str__(self) :
        return f"{self.nome},{self.areasaber},{self.curso}"
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_Plural = "Diciplinas"
        
class Ocupacao(models.Model):
    nome = models.CharField (max_length = 100 , verbose_name = "Nome da Ocupacao")
    def __str__(self):
        return self.nome
    class Meta :
        verbose_name = "Ocupacao"
        verbose_name_plural = "Ocupacoes"
        
class  Pessoa (models.Model) :
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Pessoa") 
    pai = models.CharField(max_length = 100, verbose_name = "Nome do Pai ")
    mae = models.CharField(max_length = 100, verbose_name = "Nome da Mae")   
    cpf = models.CharField(max_length = 100, verbose_name = "N° do CPF")
    data_nasc = models.DateField(max_length = 100 , verbose_name = "Data de Nascimento")
    email = models.CharField(max_length = 100 , verbose_name = "Nome do seu Email")
    cidade = models.ForeignKey(Cidade, on_delete = models.CASCADE,verbose_name = "Nome da Cidade" )
    ocupacao = models.ForeignKey(Ocupacao, on_delete = models.CASCADE,verbose_name = "Nome da Ocupacao"  )
    def __str__(self) :
        return f"{self.nome},{self.pai},{self.mae},{self.cpf},{self.data_nasc},{self.email},{self.cidade},{self.ocupacao}"
    class Meta :
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        
class Periodo (models.Model): 
    periodo = models.CharField(max_length = 100, verbose_name = "N° de periodo")  
    def __str__(self):
        return self.periodo
    class Meta :
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
        
class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE,verbose_name = "Nome da Instituicao")    
    curso = models.ForeignKey(Curso,on_delete = models.CASCADE, verbose_name = "Nome do Curso" )    
        
    
        