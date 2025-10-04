# 🚀 Desafio DevOps ITEP 

## 📌 Descrição  
Este projeto implementa uma **solução containerizada** utilizando Docker e Docker Compose para orquestrar duas aplicações web Flask, acessíveis através de um **reverse proxy Nginx**.  

A ideia é simular uma arquitetura de microsserviços simples, onde cada aplicação roda isolada em seu container, mas todas são acessadas por uma única porta (80), com roteamento baseado em path (`/app1`, `/app2`).  

## 🛠️ Tecnologias  

- **🐳 Docker**: Containerização e isolamento de serviços  
- **🎼 Docker Compose**: Orquestração de múltiplos containers  
- **🐍 Flask**: Framework web minimalista em Python  
- **🔄 Nginx**: Reverse proxy e balanceador de carga  
- **🐧 Alpine Linux**: Base leve e segura para containers  
- **📋 Makefile**: Automação de build, deploy e testes  
- **🔍 Health Checks**: Monitoramento da saúde dos serviços  
- **🌐 Docker Networks**: Rede interna entre containers  

## 🏗️ Arquitetura da Solução  

```
Internet → Porta 80 → Nginx (reverse proxy) → Flask Apps
```

- `localhost/` → Página inicial  
- `localhost/app1` → App1 (Flask)  
- `localhost/app2` → App2 (Flask)  

A comunicação entre containers é feita por **nome de serviço** (service discovery do Docker), evitando o uso de IPs fixos.  

## ▶️ Como Executar  

### Opção 1: Rápida  
```bash
git clone [seu-repositorio]
cd DesafioDevOPS
docker-compose up
```

### Opção 2: Com Makefile  
```bash
make help    # lista os comandos disponíveis
make start   # build + up + test
make dev     # modo desenvolvimento
make prod    # modo produção
make test    # testar endpoints
make logs    # ver logs em tempo real
make clean   # limpar tudo
```

### Teste os Endpoints  
- **Página Principal** → [http://localhost/](http://localhost/)  
- **App1** → [http://localhost/app1](http://localhost/app1)  
- **App2** → [http://localhost/app2](http://localhost/app2)  

## ⚙️ Decisões Técnicas  

- **Nginx como proxy**: simples, rápido, consolidado em produção.  
- **Flask para apps**: leve, flexível e ideal para microsserviços simples.  
- **Imagens slim/alpine**: menores, seguras e mais rápidas.  
- **Rede bridge customizada**: comunicação segura entre serviços.  
- **Health checks**: garantem que o proxy só suba quando os apps estiverem prontos.  

## 🚧 Dificuldades e Soluções  

1. **Health check sem `curl`** → adicionei instalação manual.  
2. **Proxy iniciando antes das apps** → usei `depends_on` com healthcheck dentro do docker compose para app1 e app2.  
3. **IPs variando entre containers** → a primeira tentativa usava IPs fixos e foi resolvido com service discovery do Docker.  
4. **Problemas de headers** → foram depois configurados corretamente no Nginx.  
5. **Debugging** → padronizei logs, comandos no Makefile e uso de `docker-compose exec`.  

## 📚 O que Aprendi  

- **Diferença entre Dockerfile, Imagem, Container e Docker Compose**  
  - **Dockerfile** → instruções para criar a imagem  
  - **Imagem** → “receita pronta” (base imutável)  
  - **Container** → instância em execução da imagem  
  - **Docker Compose** → orquestra múltiplos containers  

- **Práticas de containerização**: isolamento, redes internas e service discovery.  
- **Orquestração com Compose**: dependências, health checks e variáveis de ambiente.  
- **Configuração de proxy reverso** com Nginx. 
- **Definição de Headers** Aprendi o que são headers (informações da comunicação HTTPS) a e a importância de configurá-los no Nginx. 
- **Automação** com Makefile e no geral boas práticas de DevOps.  

## 🔮 Melhorias Futuras  

- Implementar **HTTPS (SSL/TLS)**.  
- Executar containers com **usuário não-root**.  
- Adicionar **monitoramento (Prometheus/Grafana)**.  
- Criar **pipeline CI/CD com GitHub Actions**.  
- Usar **multi-stage builds** para imagens menores e mais leves.  