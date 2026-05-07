# Azure Architect Interview Questions & Answers

## ✅ 1. How do you design a highly available and scalable application on Azure?

**Answer:**
- Use **Availability Zones** for zone-level resilience
- Deploy across **multiple regions** (active-active / active-passive)
- Use **Azure Front Door / Application Gateway / Load Balancer**
- Enable **auto-scaling** (VMSS, AKS, App Service)
- Design **stateless applications** with external storage

**Example Architecture:**
Front Door → App Gateway → App Service → Azure SQL + Redis Cache

---

## ✅ 2. Availability Set vs Zones vs Region Pairs

| Feature | Availability Set | Availability Zone | Region Pair |
|--------|----------------|------------------|-------------|
| Scope | Datacenter | Multiple DCs | Geography |
| Use case | VM redundancy | Critical apps | Disaster recovery |
| Fault isolation | Rack | Entire DC | Region |

**Tip:**  
Use **Zones for HA**, **Region Pairs for DR**

---

## ✅ 3. When to use VMs vs App Service vs AKS vs Functions?

- **VMs:** Full control, legacy apps  
- **App Service:** Web apps, APIs (PaaS)  
- **AKS:** Microservices & containers  
- **Functions:** Event-driven serverless  

**Rule:**  
- Minimal management → App Service / Functions  
- Complex architecture → AKS  
- Legacy → VM  

---

## ✅ 4. Disaster Recovery Design

- Define **RTO & RPO**
- Use **Geo-redundant storage (GRS)**
- Deploy in **secondary region**
- Use **Azure Site Recovery**
- Route via **Traffic Manager / Front Door**

**Models:**
- Active-Passive
- Active-Active

---

## ✅ 5. Networking Components

- **VNet:** Private network
- **NSG:** Layer 4 filtering (IP/Port)
- **Azure Firewall:** Layer 7 centralized security

**Best Practice:**
- NSG → subnet level  
- Firewall → perimeter  

---

## ✅ 6. VNet Peering vs VPN vs ExpressRoute

- **VNet Peering:** Azure backbone, low latency  
- **VPN Gateway:** Internet-based  
- **ExpressRoute:** Private dedicated connection  

**Use Case:**
- Enterprise → ExpressRoute  
- Hybrid quick setup → VPN  

---

## ✅ 7. Storage Types

- **Blob:** Object storage  
- **File:** Shared file system  
- **Queue:** Messaging  
- **Table:** NoSQL  

**Redundancy:**
- LRS → Local  
- ZRS → Zone  
- GRS → Region  

---

## ✅ 8. Cosmos DB vs Azure SQL

| Feature | Cosmos DB | Azure SQL |
|--------|----------|-----------|
| Type | NoSQL | Relational |
| Scale | Global | Regional |
| Schema | Flexible | Fixed |

**Use Cosmos DB For:**
- Global apps  
- High throughput  
- Low latency  

---

## ✅ 9. Managed Identity

- Provides identity for Azure services
- Removes need to store credentials
- Integrated with **Key Vault & RBAC**

**Example:**
App → Managed Identity → Key Vault

---

## ✅ 10. CI/CD Design

- Use **Azure DevOps / GitHub Actions**
- CI → Build, test  
- CD → Deploy  

**Practices:**
- Blue-Green / Canary deployments  
- Infrastructure as Code (Bicep/Terraform)  
- Key Vault for secrets  

---

## ✅ 11. Monitoring Tools

- **Azure Monitor**
- **Log Analytics**
- **Application Insights**

**Best Practice:**
- Alerts + dashboards + tracing  

---

## ✅ 12. High Availability (99.99%)

- Multi-zone deployment  
- Load balancing  
- Auto-scaling  
- Stateless services  
- DB replication  

**Patterns:**
- Retry  
- Circuit breaker  

---

## ✅ 13. RPO vs RTO

- **RPO:** Data loss tolerance  
- **RTO:** Recovery time  

**Example:**
- RPO = 5 min  
- RTO = 10 min  

---

## ✅ 14. Event-Driven Architecture

- **Event Grid:** Event routing  
- **Service Bus:** Reliable messaging  
- **Event Hub:** Streaming  

**Flow:**
Producer → Event → Consumer  

---

## ✅ 15. Cost Optimization

- Reserved instances  
- Auto-scaling  
- Stop unused VMs  
- Spot VMs  
- Azure Cost Management  

---

## ✅ 16. Multi-Tenant Design

- Shared DB  
- Separate schema  
- Separate DB per tenant  

**Decision Based On:**
- Security  
- Cost  
- Scalability  

---

## ✅ 17. E-commerce Architecture (Example)

- Front Door  
- App Gateway (WAF)  
- AKS / App Service  
- Azure SQL / Cosmos DB  
- Redis Cache  
- Service Bus  
- Blob Storage  
- CDN  

---

## ✅ 18. Migration Strategy

- Rehost (Lift & Shift)  
- Refactor  
- Rearchitect  

**Steps:**
Assess → Plan → Migrate → Optimize  

---

# 🔥 Final Tips

- Always explain **trade-offs**
- Focus on **scalability, security, cost**
- Be ready to **draw architecture diagrams**
- Expect “Why this service?” follow-ups
