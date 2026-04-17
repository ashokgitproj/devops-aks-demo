# devops-aks-demo

[![CI Frontend](https://github.com/ashokgitproj/devops-aks-demo/actions/workflows/ci-frontend.yaml/badge.svg)](https://github.com/ashokgitproj/devops-aks-demo/actions/workflows/ci-frontend.yaml)
[![CI Backend](https://github.com/ashokgitproj/devops-aks-demo/actions/workflows/ci-backend.yaml/badge.svg)](https://github.com/ashokgitproj/devops-aks-demo/actions/workflows/ci-backend.yaml)

Enterprise-grade microservices deployment on Azure Kubernetes Service (AKS).

## Architecture
- **App**: 3-service microservices (frontend · backend · Redis)
- **Cluster**: AKS with Azure CNI, OIDC, Workload Identity
- **Networking**: Hub-Spoke VNet, Istio service mesh, mTLS
- **CI/CD**: GitHub Actions (per-service CI) + ArgoCD GitOps (CD)
- **Security**: UAMI, Key Vault CSI, Trivy, SonarCloud
- **Observability**: Dynatrace, Azure Monitor

## Repository structure

.
├── apps/               # Application source code
│   ├── frontend/       # React + Nginx
│   ├── backend/        # Python FastAPI
│   └── redis/          # Redis config
├── charts/             # Helm charts (one per service)
│   ├── frontend/
│   ├── backend/
│   └── redis/
├── infra/              # Azure provisioning scripts
│   ├── scripts/        # Ordered shell scripts (00-07)
│   └── policies/       # Azure Policy definitions
├── .github/
│   └── workflows/      # CI/CD pipeline definitions
└── docs/               # Architecture docs and runbooks

## Phases
| Phase | Topic | Status |
|-------|-------|--------|
| 0 | Foundations — repo, Azure infra, identity | 🔄 In progress |
| 1 | AKS provisioning + network policies | ⏳ Pending |
| 2 | CI pipelines (per-service, OIDC, scan-gated) | ⏳ Pending |
| 3 | CD pipeline (Helm, environment-aware) | ⏳ Pending |
| 4 | Istio service mesh | ⏳ Pending |
| 5 | App deployment + K8s troubleshooting | ⏳ Pending |
| 6 | Observability — Dynatrace + Azure Monitor | ⏳ Pending |
| 7 | GitOps — ArgoCD App of Apps | ⏳ Pending |
| 8 | Agentic AI — MCP server | ⏳ Pending |
