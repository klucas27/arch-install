<img align="center" alt="arch" src="files/Arch_Start.png" />
<h4>Script para a instalação do Arch Linux</h4> 

<div>
    <h2>* Menu Iniciar *</h2>
    <p>O menu é composto por duas opções
 de instalação, [1] Padrão (Definida pelo desenvolvedor), e a opção da instalação pre configurada 
(configurações como: teclado, localização, etc.).</p>
    <ul>    
        <li>Instalação Padrão(opção [1])</li>
            <p> Na Instalação padrão sera instalada o sistema Arch Linux com: </p>
            <ul>
                <li> Softwares para devs </li>
                <li> Grub Customizado </li>
                <li> Grub configurada para o tipo BIOS </li>
                <li> Interface gráfica Budgie </li>
                <li> Display Manager LXDM </li>
                <li> Configuração do Mirror List para Brazil </li>
                <li> Localização America/Sao_Paulo </li>
                <li> Layout do Teclado BR </li>
                <li> Variante ABNT2 </li>
                <li> Linguagem pt_BR </li>
                <li> Codificação UTF-8 </li>
                <li> 55% de espaço do disco para o /root</li>
                <li> 55% a 96% de espaço do disco para o /home</li>
            </ul>
        <p></p>
        <li> Instalação Customizada(opção [2])</li>
            <p>Na instalação customizada todas configurações da instalação Padrão poderão ser alteradas.</p>
    </ul>
    <h2> * Instalação *</h2>
    <h4> Passo 1: </h4>
    <p>Faça boot com o sistema arch linux (sua ISO pode ser baixada no site oficial).</p>
    <h4> Passo 2: </h4>
    <p>Faça o download e a instalação do git:</p>
    
    $ pacman -Sy git --noconfirm

<h4> Passo 3: </h4>
    <p>Faça o download deste repositório:</p>
    
    # git clone https://github.com/klucas27/arch-install

<h4> Passo 4: </h4>
    <p>Entre dentro da pasta baixada(arch-install):</p>
    
    # cd arch-install

<h4> Passo 5: </h4>
    <p>Execute o script: </p>
    
    # python3 start.py

<p>Deste modo começara o processo de instalação.</p>

</div>