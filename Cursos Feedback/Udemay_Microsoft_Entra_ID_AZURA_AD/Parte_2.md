

You do not have to do all of this stuff with setting up Hyper-V virtual machines, unless you are interested

in learning the interconnect sync section further down in the course.


# Hyper-v

💽 Hyper-V é o hipervisor nativo da Microsoft — ou seja, uma ferramenta que cria e gerencia máquinas virtuais (VMs) no Windows.

💸 É gratuito?

Sim, é gratuito em várias formas:

Windows 10/11 Pro ou Enterprise: vem incluso, só precisa ativar.

🚀 Como usar (resumo prático):

Ative o recurso:

dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All


ou vá em Painel de Controle → Programas → Ativar ou desativar recursos do Windows → Hyper-V.

Reinicie o PC.

Abra o Gerenciador do Hyper-V (busque no menu iniciar).

Crie uma nova máquina virtual:

Escolha nome, memória RAM, tipo de disco virtual (VHDX) e ISO do sistema que vai instalar.

Inicie a VM e instale o sistema normalmente.

⚖️ Pontos bons:

✅ Nativo no Windows
✅ Estável e rápido
✅ Suporta Windows e Linux
✅ Integrado com PowerShell

⚠️ Pontos ruins:

❌ Não roda em versões Home do Windows
❌ Interface mais “corporativa” e menos amigável que VirtualBox
❌ Não é ideal pra quem quer GPU passthrough (pra jogos, por exemplo)


https://learn.microsoft.com/en-us/windows-server/virtualization/hyper-v/get-started/install-hyper-v?tabs=powershell&pivots=windows-server