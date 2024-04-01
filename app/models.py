from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length = 100, verbose_name = "Nome da Cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    
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
    carga_horaria_total = models.CharField(max_length = 100 , verbose_name = "N° de Horas no Total")  
    
    duracao_meses =  models.CharField(max_length = 100 , verbose_name = "N° de meses") 
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
        verbose_name_plural = "Diciplinas"
        
class Ocupacao(models.Model):
    nome = models.CharField (max_length = 100 , verbose_name = "Nome da Ocupacao")
    def __str__(self):
        return self.nome
    class Meta:
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
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"
        
class Periodo (models.Model): 
    periodo = models.CharField(max_length = 100, verbose_name = "N° de periodo")  
    def __str__(self):
        return self.periodo
    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
        
class Matricula(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete = models.CASCADE,verbose_name = "Nome da Instituicao")    
    
    curso = models.ForeignKey(Curso,on_delete = models.CASCADE, verbose_name = "Nome do Curso" ) 
    
    pessoa = models.ForeignKey(Pessoa, on_delete = models.CASCADE, verbose_name = "Nome da Pessoa")   
    
    data_inicio = models.DateField(verbose_name = "Data de inicio")  
    data_previsao_termino = models.DateField(verbose_name = "Data de Previsão de Termino")      
    def __str__(self) :
        return f"{self.instituicao},{self.curso},{self.pessoa}{self.data_inicio},{self.data_previsao_termino}"
    class Meta:
        verbose_name_plural = "Matriculas"
        verbose_name : "Matrícula"
        
class Avaliacao (models.Model):
    descricao = models.CharField(max_length = 100, verbose_name = "Nome da Avaliação")    
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE,verbose_name = "Nome do Curso")
    
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Nome da Disciplina")   
    
    pessoa = models.ForeignKey(Pessoa,on_delete = models.CASCADE,verbose_name = "Nome da Pessoa")
    
    def __str__(self):
        return f"{self.descricao},{self.curso},{self.disciplina},{self.pessoa}"
    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural = "Avaliacoes"
        
class Frequencia(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE,verbose_name = "Nome do Curso")
    
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Nome da Disciplina") 
    
    numero_faltas = models.CharField(max_length = 100, verbose_name = "Numero de Faltas")
    
    pessoa = models.ForeignKey(Pessoa,on_delete = models.CASCADE,verbose_name = "Nome da Pessoa")
    
    def __str__(self):
        return f"{self.curso},{self.disciplina},{self.numero_faltas},{self.pessoa}"
    
    class Meta:
        verbose_name = "Frequencia"
        verbose_name_plural = "Frequencias"
    
class Turma(models.Model):
    nome = models.CharField(max_length = 100,verbose_name = "Nome da Turma")
    
    periodo = models.CharField(max_length = 100, verbose_name = "Nome do Período")        
    
    def __str__(self):
        return f"{self.nome},{self.periodo}"
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        
class Ocorrencia(models.Model):
    descricao = models.CharField(max_length = 100, verbose_name = "Nome da Descrição" )
    
    data = models.DateField(verbose_name = "Data da Ocorrencia")
    
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE,verbose_name = "Nome do Curso")
    
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Nome da Disciplina") 
    
    pessoa = models.ForeignKey(Pessoa,on_delete = models.CASCADE,verbose_name = "Nome da Pessoa")
    
    def __str__(self) :
        return f"{self.descricao},{self.data},{self.curso},{self.disciplina},{self.pessoa}"
    
    class Meta:
        verbose_name = "Ocorrencia"
        verbose_name_plural = "Ocorrencias"
            
class DisciplinaCurso(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete = models.CASCADE, verbose_name = "Nome da Disciplina") 
    
    carga_horaria = models.CharField(max_length = 100, verbose_name = "Nome Carga Horaria")
    
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE,verbose_name = "Nome do Curso")
    
    periodo = models.ForeignKey(Periodo,on_delete = models.CASCADE, verbose_name = "Nome do periodo")  
    
    def __str__(self) :
        return f"{self.disciplina},{self.carga_horaria},{self.curso},{self.periodo}"
    
    class Meta:
        verbose_name = "DisciplinaCurso"
        verbose_name_plural = "DisciplinaCursos"
        
class TiposAvaliacao(models.Model):    
    nome = models.CharField(max_length = 100,verbose_name = "Nome da Avaliacao")
    
    def __str__(self) :
        return self.nome
    
    class Meta:
        verbose_name = "TiposAvaliacao"
        verbose_name_plural = "TiposAvaliacoes"
    