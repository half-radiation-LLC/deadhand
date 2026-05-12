# Deadhand Protocol: Software Bill of Materials (SBOM)
**Version:** 1.0.0-Sovereign  
**Date:** May 12, 2026  
**Status:** AUDIT-READY  

---

## 1. Project Identity
| Field | Value |
| :--- | :--- |
| **Product Name** | Deadhand Sovereign Protocol |
| **Vendor** | half radiation LLC |
| **Core License** | AGPL-3.0 (Sovereign Grant) |
| **Architecture** | Hybrid Desktop (Local Secrets) + Cloud Heartbeat (Distributed Shards) |

---

## 2. Cryptographic Core (Local-First)
These components handle the splitting and encryption of seed phrases. They are strictly local and never transmit raw data to the cloud.

| Component | Description | Version | License |
| :--- | :--- | :--- | :--- |
| **Shamir’s Secret Sharing** | 2-of-3 threshold secret splitting | Custom (v1.2) | MIT |
| **AES-256-GCM** | Authenticated encryption for stored shards | Cryptography 42.x | BSD/Apache |
| **SHA-256** | Integrity verification and identity hashing | Python Standard | PSF |
| **BIP-39** | Mnemonic phrase support/compatibility | Python Standard | PSF |

---

## 3. Sovereign Desktop Client
Built for the power-user who demands local autonomy and "Obsidian-grade" aesthetics.

| Package | Purpose | Category |
| :--- | :--- | :--- |
| `customtkinter` | UI Framework (Modern Dark Mode) | Frontend |
| `pillow` | Image processing for Visual Steganography | Media |
| `pyinstaller` | Binary packaging and standalone distribution | DevTools |
| `python-dotenv` | Local environment and configuration management | Core |

---

## 4. Sovereign Backend & Gateway
The hardened infrastructure that manages the "Pulse" (heartbeats) and "Fuse" (licenses).

| Package | Purpose | Category |
| :--- | :--- | :--- |
| `fastapi` | High-performance ASGI web framework | Server |
| `uvicorn` | Production-grade ASGI server implementation | Server |
| `x402` | Sovereign crypto paywall protocol (Base/EVM) | Payments |
| `sqlalchemy` | ORM for secure database interactions | Data |
| `psycopg2-binary` | Postgres adapter for Neon DB connectivity | Data |
| `jinja2` | Secure template engine for server-side pages | UX |

---

## 5. Distributed Infrastructure (Cloud Dependencies)
Minimalist dependencies used for protocol dispatching and verification.

| Provider | Purpose | Status |
| :--- | :--- | :--- |
| **Neon** | Serverless Postgres (Data Persistency) | Active |
| **Resend** | Transactional Email Dispatch (Beneficiary Alert) | Active |
| **PostHog** | Privacy-focused usage telemetry | Optional |
| **PayAI** | x402 Facilitator (Payment Verification) | Active |

---

## 6. Regulatory & Security Posture
- **Data Residency:** Critical secrets (Shard A & Shard B) never leave the user's hardware.
- **Privacy:** Telemetry is anonymized and strictly limited to application health.
- **Protocol Portability:** The SSS and BIP-39 implementations are standard, allowing recovery even if half radiation LLC ceases operations.

---
*End of SBOM*
