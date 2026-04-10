from flask import Flask, request, redirect, session, render_template_string
from datetime import datetime
import os

app = Flask(**name**)
app.secret_key = "segredo"

usuarios = {"admin": "123"}

procedimentos = []
tarefas = []

# LOGIN

@app.route("/", methods=["GET", "POST"])
def login():
if request.method == "POST":
user = request.form["usuario"]
senha = request.form["senha"]
if user in usuarios and usuarios[user] == senha:
session["user"] = user
return redirect("/dashboard")
return render_template_string(""" <h2>Login</h2> <form method="post">
Usuário: <input name="usuario"><br>
Senha: <input name="senha" type="password"><br> <button>Entrar</button> </form>
""")

# DASHBOARD

@app.route("/dashboard")
def dashboard():
if "user" not in session:
return redirect("/")

```
alertas = [
    t for t in tarefas 
    if t["status"] != "concluído" and datetime.strptime(t["prazo"], "%Y-%m-%d") < datetime.now()
]

return render_template_string("""
<h2>Dashboard</h2>
<a href="/novo_procedimento">Novo Procedimento</a><br><br>

<h3>⚠️ Alertas</h3>
{% for a in alertas %}
    <p>{{a["descricao"]}} - ATRASADO</p>
{% endfor %}

<h3>Procedimentos</h3>
{% for p in procedimentos %}
    <p>
        {{p["titulo"]}} - {{p["status"]}}
        <a href="/procedimento/{{loop.index0}}">Abrir</a>
    </p>
{% endfor %}
""", procedimentos=procedimentos, alertas=alertas)
```

# NOVO PROCEDIMENTO

@app.route("/novo_procedimento", methods=["GET", "POST"])
def novo_procedimento():
if request.method == "POST":
procedimentos.append({
"titulo": request.form["titulo"],
"status": "em andamento",
"relatorio": "",
"oitiva": ""
})
return redirect("/dashboard")

```
return render_template_string("""
<h2>Novo Procedimento</h2>
<form method="post">
    Título: <input name="titulo"><br>
    <button>Criar</button>
</form>
""")
```

# DETALHE DO PROCEDIMENTO

@app.route("/procedimento/[int:id](int:id)", methods=["GET", "POST"])
def detalhe(id):
p = procedimentos[id]

```
if request.method == "POST":
    p["relatorio"] = request.form["relatorio"]
    p["oitiva"] = request.form["oitiva"]

tarefas_proc = [t for t in tarefas if t["proc_id"] == id]

return render_template_string("""
<h2>{{p["titulo"]}}</h2>

<form method="post">
    <h3>Relatório</h3>
    <textarea name="relatorio" rows="5" cols="40">{{p["relatorio"]}}</textarea>

    <h3>Oitiva</h3>
    <textarea name="oitiva" rows="5" cols="40">{{p["oitiva"]}}</textarea>

    <br><button>Salvar</button>
</form>

<h3>Tarefas</h3>
{% for t in tarefas %}
    <p>{{t["descricao"]}} - {{t["status"]}} (Prazo: {{t["prazo"]}})</p>
{% endfor %}

<a href="/nova_tarefa/{{id}}">Nova Tarefa</a><br>
<a href="/dashboard">Voltar</a>
""", p=p, tarefas=tarefas_proc)
```

# NOVA TAREFA

@app.route("/nova_tarefa/[int:id](int:id)", methods=["GET", "POST"])
def nova_tarefa(id):
if request.method == "POST":
tarefas.append({
"proc_id": id,
"descricao": request.form["descricao"],
"prazo": request.form["prazo"],
"status": "pendente"
})
return redirect(f"/procedimento/{id}")

```
return render_template_string("""
<h2>Nova Tarefa</h2>
<form method="post">
    Descrição: <input name="descricao"><br>
    Prazo: <input type="date" name="prazo"><br>
    <button>Criar</button>
</form>
""")
```

if **name** == "**main**":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
