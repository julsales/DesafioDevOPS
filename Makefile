
.PHONY: help build up down logs clean test restart status

help: ## Mostra esta mensagem de ajuda
	@echo "Desafio DevOps - ITEP"
	@echo "===================="
	@echo ""
	@echo "Comandos disponíveis:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""

build: ## Constrói todas as imagens Docker
	@echo "🔨 Construindo imagens Docker..."
	docker-compose build

up: ## Inicia todos os serviços
	@echo "🚀 Iniciando serviços..."
	docker-compose up -d
	@echo "✅ Serviços iniciados!"
	@echo "🌐 Acesse: http://localhost"

down: ## Para todos os serviços
	@echo "🛑 Parando serviços..."
	docker-compose down
	@echo "✅ Serviços parados!"

logs: ## Mostra logs de todos os serviços
	docker-compose logs -f

logs-app1: ## Mostra logs do app1
	docker-compose logs -f app1

logs-app2: ## Mostra logs do app2
	docker-compose logs -f app2

logs-proxy: ## Mostra logs do proxy
	docker-compose logs -f proxy

restart: ## Reinicia todos os serviços
	@echo "🔄 Reiniciando serviços..."
	docker-compose restart
	@echo "✅ Serviços reiniciados!"

status: ## Mostra status dos containers
	@echo "📊 Status dos containers:"
	docker-compose ps

test: ## Testa se os serviços estão funcionando
	@echo "🧪 Testando serviços..."
	@echo "Testando página principal..."
	@curl -s -o /dev/null -w "Status: %{http_code}\n" http://localhost/ || echo "❌ Falha na página principal"
	@echo "Testando App1..."
	@curl -s -o /dev/null -w "Status: %{http_code}\n" http://localhost/app1 || echo "❌ Falha no App1"
	@echo "Testando App2..."
	@curl -s -o /dev/null -w "Status: %{http_code}\n" http://localhost/app2 || echo "❌ Falha no App2"
	@echo "✅ Testes concluídos!"

clean: ## Remove containers, imagens e volumes
	@echo "🧹 Limpando ambiente..."
	docker-compose down -v --rmi all --remove-orphans
	@echo "✅ Ambiente limpo!"

dev: ## Inicia em modo de desenvolvimento com rebuild
	@echo "🔧 Iniciando em modo desenvolvimento..."
	docker-compose up --build

prod: build up ## Inicia em modo produção

# Constrói e inicia tudo
start: build up test ## Comando completo: build + up + test

# Desenvolvimento rápido
dev-rebuild: down build up ## Para, reconstrói e inicia