# 🧩 Resumo – Ansible: Utilidade e Aplicabilidade 🚀

O Ansible é uma ferramenta de automação de TI usada para gerenciar configurações, implantar aplicações, orquestrar tarefas complexas e administrar infraestruturas inteiras — tudo isso de forma simples, rápida e sem dor de cabeça 💻✨
**🕵️ Esse camarada vai montar e conectar seus servidores para acelerar, tudo via shell, pratico e confiavel, a base dos sistemas modernos.**

## 🛠️ Utilidade Principal

🔁 Automação de tarefas repetitivas: Adeus comandos manuais infinitos! O Ansible executa tudo de uma vez só.

⚙️ Gerenciamento de configuração: Mantém todos os servidores iguais, do sistema até as permissões. **🕵️Tudo customizavel, separando em grupos, cadeias,

🤖 Orquestração: Coordena várias máquinas ao mesmo tempo — ideal pra deploys e clusters.

🌐 Provisionamento: Cria e prepara ambientes completos (servidores, VMs, containers) com um único comando.

## 🌍 Aplicabilidade

🧠 DevOps & CI/CD: Perfeito para pipelines automatizados com Jenkins, GitLab CI e similares.

🧾 Infraestrutura como Código (IaC): Toda a config é escrita em YAML, legível e versionável.

☁️ Ambientes Cloud & híbridos: Funciona com AWS, Azure, GCP, VMware, Proxmox e até bare-metal.

🔒 Segurança e Compliance: Aplica patches, políticas e hardening em escala — rápido e padronizado.

## ⚙️ Diferenciais

🕵️‍♂️ Sem agentes: Não precisa instalar nada nas máquinas gerenciadas — usa SSH (ou WinRM no Windows).

🧩 Fácil de aprender: YAML é simples e direto — até quem odeia sintaxe complicada ama ❤️.  **🕵️:Esse treco é um primo do python, direto igual uma criança, Zero verbo.**

🔄 Extensível: Usa Módulos, Roles e Playbooks pra criar automações reutilizáveis e elegantes.

## Documentação 

**[>Documentação<](https://docs.ansible.com/)**

# 📚 Terminologias do Ansible 🤖

## 🧠 1️⃣ Control Node - Tua maquina
• 💬 É a máquina de comando, onde o Ansible está instalado.
• É daqui que tu envia as ordens para os outros servidores.
• Pode ser teu notebook, um servidor central, ou uma VM dedicada
🕵️: O coração da operação, a unica maquina que precisa do ansible para tudo funcionar, é dela que vamos dispara os comandos e controlar tuda.

## 🌐 2️⃣ Managed Node - Maquina operada remotamente
🕵️ : Todo tipo de equipamento que de para ser acessado via SSH/WinRM, se aceita receber um comando podemos operar automaticamente.
• São os alvos que o Ansible gerencia.
• Ele acessa cada nó via SSH (Linux) ou WinRM (Windows).

## 🧾 3️⃣ Inventory
🕵️ : Perceba a simplicidade disso, poderia ser um arquivo Txt, ao separar em bloquinhos podemos crescer exponencialmente mas com um controle solido. Só não deixar o estagiario ter acesso a isso, pelo amor do Codigo.
• É o arquivo que lista todos os Managed Nodes.
• Pode ser um .ini, .yaml, ou até dinâmico (buscando da AWS, por exemplo).

Exemplo:
[webservers]
web01 ansible_host=192.168.1.10
web02 ansible_host=192.168.1.11

📎 É tipo a agenda de contatos do Ansible. ☎️

## 📜 4️⃣ Playbook - TRABALHE MAQUINA
🕵️ : Aqui você manda e a maquina obedece, é o arquivo que vai ter as ordens, vc as direciona por grupo(O inventario ali de cima).
• É o coração do Ansible ❤️
• Um arquivo .yml com uma sequência de tarefas (plays) que dizem o que fazer e onde fazer.
• Cada play descreve ações aplicadas a um grupo de hosts.

📍Exemplo:
- name: Atualizar pacotes e habilitar firewall
  hosts: webservers
  tasks:
    - name: Atualizar pacotes
      apt:
        upgrade: yes

## 🔧 5️⃣ Task
🕵️ : Cada celula de comando, o comando automatizado, elegante e sem stress.
• Cada ação individual dentro de um playbook.
• Pode instalar pacotes, editar arquivos, iniciar serviços etc.

📍Exemplo:

 name: Instalar o Nginx
  apt:
    name: nginx
    state: present
.



## 🧩 6️⃣ Módulo
• São os blocos de construção do Ansible.
• Cada módulo executa uma tarefa específica (ex: apt, yum, copy, service, user, ufw etc).
• Tu chama módulos dentro das tasks.
📍Exemplo:

- name: Criar um novo usuário
  user:
    name: bernardo
    state: present

⚙️ Os módulos são como “ferramentas prontas” dentro da caixa do Ansible.

## 🗃️ 7️⃣ Role

• Um pacote organizado de automação.
• Agrupa tasks, handlers, variáveis e templates em uma estrutura padronizada.
• Ideal pra reuso e organização de projetos grandes.
📍Exemplo de estrutura:
roles/
├── webserver/
│   ├── tasks/
│   │   └── main.yml
│   ├── templates/
│   ├── handlers/
│   └── vars/
📎 Roles são como mini projetos modulares dentro do Ansible.

## 🧮 8️⃣ Variable (Variável)

Valores dinâmicos que tu pode usar nos playbooks.

Tornam o código flexível e reutilizável.

📍Exemplo:

vars:
  pacote_web: nginx

tasks:
  - name: Instalar pacote
    apt:
      name: "{{ pacote_web }}"
      state: present


🔁 Evita repetir informações e facilita ajustes.

## 🧱 9️⃣ Template

Arquivos de configuração com variáveis dinâmicas, processados pelo Ansible usando Jinja2 (.j2).

Muito usado pra gerar configs personalizadas.

📍Exemplo (nginx.conf.j2):

server_name {{ dominio }};
listen 80;


💡 O Ansible substitui {{ dominio }} pelo valor da variável e copia pro servidor.

## 🔔 🔟 Handler

São tasks especiais que só rodam quando algo muda.

Usado, por exemplo, pra reiniciar um serviço depois que um arquivo é alterado.

📍Exemplo:

tasks:
  - name: Copiar configuração
    copy:
      src: nginx.conf
      dest: /etc/nginx/nginx.conf
    notify:
      - Reiniciar nginx

handlers:
  - name: Reiniciar nginx
    service:
      name: nginx
      state: restarted


📎 Handlers garantem eficiência — nada de reiniciar serviço à toa.

## 🧰 1️⃣1️⃣ Collection

Um pacote completo que inclui roles, módulos, plugins e playbooks prontos pra uso.

Instalável via ansible-galaxy.

📍Exemplo:

ansible-galaxy collection install community.general


🧙 As collections são tipo bibliotecas mágicas de automação.

## 🧩 1️⃣2️⃣ Facts

São informações coletadas automaticamente sobre cada servidor (SO, IP, CPU, memória, etc.).

Podem ser usadas dentro dos playbooks.

📍Exemplo:

- debug:
    msg: "O servidor tem {{ ansible_processor_cores }} núcleos."


📎 Facts = dados em tempo real sobre teu ambiente.

## 🧭 1️⃣3️⃣ Ad-Hoc Commands

Comandos rápidos, executados diretamente sem playbook.

Úteis pra tarefas simples ou testes.

📍Exemplo:

ansible all -i inventory.ini -m ping
ansible webservers -i inventory.ini -m apt -a "name=nginx state=present"


💡 É tipo o modo “comando rápido” do Ansible.

## 💬 1️⃣4️⃣ Vault

Ferramenta pra criptografar senhas e dados sensíveis dentro de playbooks.

Segurança 💪

📍Exemplo:

ansible-vault create secrets.yml
ansible-playbook playbook.yml --ask-vault-pass


🔐 Nada de senhas em texto puro, pelo amor da cibersegurança.