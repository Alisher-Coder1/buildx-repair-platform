# 28 — Roadmap to MVP and Production
## Document Control Metadata

| Field | Value |
|---|---|
| Document ID | DOC_28 |
| File Name | `28_roadmap_to_mvp_and_production.md` |
| Version | v0.1 |
| Status | DRAFT |
| Created | 2026-04-29 |
| Owner | Documentation Architect |
| Customer Role | Product Owner / Заказчик |
| Executor Role | Documentation Architect / Implementation Executor |
| Hierarchy Level | Level 6 — Planning / Delivery Strategy |
| Implementation Block | Roadmap from zero to prototype, MVP, pilot, production |
| Criticality | HIGH |

---

## 1. Purpose

Этот документ фиксирует путь внедрения продукта с нуля до production, чтобы проект не превратился в кашу.

Главная логика:

```text
Documentation control → Lean specs → Backend prototype → Engines → UI → Prototype release → MVP hardening → Pilot → Production
```

---

## 2. Main Roadmap Principles

```text
1. Скорость важна, но только через проверяемые этапы.
2. Документация должна ускорять разработку, а не заменять продукт.
3. Новые идеи идут в backlog, а не расширяют MVP автоматически.
4. Первый рабочий vertical slice важнее десятков незавершённых модулей.
5. Каждый этап заканчивается deliverables, acceptance criteria и GitHub checkpoint.
```

---

## 3. Phase Overview

| Phase | Name | Status | Exit Gate |
|---|---|---|---|
| PHASE_0 | Product Framing / Продуктовая рамка | `PARTIAL` | Можно объяснить продукт разработчику или инвестору за 2–3 минуты без потери смысла. |
| PHASE_1 | Documentation Operating System / Операционная система документации | `IN_PROGRESS` | Можно понять, какой документ за что отвечает, какие документы связаны и какие документы читать перед реализацией модуля. |
| PHASE_2 | Lean Prototype Specifications / Минимальные спецификации прототипа | `NEXT` | Backend implementation can start. |
| PHASE_3 | Backend Prototype Core / Ядро backend-прототипа | `NOT_STARTED` | Backend создаёт проект и комнату, возвращает корректный core-summary. |
| PHASE_4 | Rule Artifacts + Deterministic Engines / Правила и расчётные движки | `NOT_STARTED` | Можно объяснить расчёт цепочкой: operation → rule → norm → formula → quantity → package_count. |
| PHASE_5 | Minimal Guided Web UI / Минимальный guided web UI | `NOT_STARTED` | Неспециалист может создать комнату и прочитать результат. |
| PHASE_6 | Prototype Integration + Release / Интеграция и выпуск Prototype v0.1 | `NOT_STARTED` | Prototype v0.1 можно показать как рабочий продуктовый срез. |
| PHASE_7 | MVP Hardening / Укрепление MVP | `NOT_STARTED` | MVP можно тестировать на нескольких реалистичных сценариях ремонта. |
| PHASE_8 | Pilot Usage / Пилотное использование | `NOT_STARTED` | Понятно, что исправлять перед production-hardening. |
| PHASE_9 | Production Hardening / Подготовка к production | `NOT_STARTED` | Можно выпускать production-ready v1 для ограниченного использования. |
| PHASE_10 | Post-MVP Expansion / Расширение после MVP | `FUTURE` | Платформа растёт слоями, а не превращается в кашу. |

---

## 4. Detailed Phase Fixation

## PHASE_0 — Product Framing / Продуктовая рамка

**Status:** `PARTIAL`  

**Goal:** Зафиксировать, что мы строим, для кого и какую реальную ценность даёт платформа.

### Deliverables

- 01_product_brief.md
- Краткое описание продукта и главной ценности
- Первичное разделение: калькулятор / дизайн / платформа управления ремонтом

### Acceptance Criteria

- Понятно, какую проблему решает продукт.
- Понятно, почему Material Consumption Engine является ядром.
- Понятно, что продукт не сводится к простому калькулятору.

### Exit Gate

Можно объяснить продукт разработчику или инвестору за 2–3 минуты без потери смысла.

### Recommended GitHub Checkpoint

```bash
git commit -m "docs: confirm product framing"
```

---
## PHASE_1 — Documentation Operating System / Операционная система документации

**Status:** `IN_PROGRESS`  

**Goal:** Создать управляемую систему документации, чтобы 60+ файлов не превратились в хаос.

### Deliverables

- 00_documentation_index.md
- 13_document_acceptance_and_governance.md
- 45_documentation_writing_methodology_and_style_guide.md
- docs/documentation_registry_v0.1.yaml
- docs/audit/documentation_audit_question_matrix_v0.1.md
- docs/audit/documentation_dependency_map_v0.1.md
- docs/cards/document_cards_v0.1.md
- docs/templates/document_template.md

### Acceptance Criteria

- Все документы 00–60 проиндексированы.
- Есть карта зависимостей.
- Есть карточки документов.
- Есть audit matrix.
- Есть правила freeze и Change Request.
- Есть запрет на бесконечное расширение документации.

### Exit Gate

Можно понять, какой документ за что отвечает, какие документы связаны и какие документы читать перед реализацией модуля.

### Recommended GitHub Checkpoint

```bash
git commit -m "docs: initialize documentation operating system"
```

---
## PHASE_2 — Lean Prototype Specifications / Минимальные спецификации прототипа

**Status:** `NEXT`  

**Goal:** Написать только те документы, без которых нельзя безопасно начать рабочий прототип.

### Deliverables

- 02_mvp_scope.md
- 05_domain_model.md
- 06_json_artifacts_spec.md
- 08_material_consumption_engine_spec.md
- 10_api_contract.md
- 26_validation_and_error_handling_spec.md
- 27_development_methodology_and_coding_standards.md

### Acceptance Criteria

- Prototype v0.1 строго ограничен.
- Сущности и поля понятны.
- JSON artifacts описаны.
- Material formulas и package_count описаны.
- API endpoints и responses описаны.
- Ошибки и no silent fallback описаны.
- Разработчик может начать backend без догадок.

### Exit Gate

Backend implementation can start.

### Recommended GitHub Checkpoint

```bash
git commit -m "docs: complete lean prototype specifications"
```

---
## PHASE_3 — Backend Prototype Core / Ядро backend-прототипа

**Status:** `NOT_STARTED`  

**Goal:** Собрать первый backend vertical slice: Project → Room → Geometry → Summaries.

### Deliverables

- FastAPI backend
- SQLite database
- Pydantic schemas
- SQLAlchemy models
- Geometry module
- Project and Room endpoints
- Basic pytest suite

### Acceptance Criteria

- API запускается локально.
- Можно создать проект.
- Можно создать комнату.
- Считаются площадь пола, потолка, стен и периметр.
- Есть тесты геометрии и базовой валидации.

### Exit Gate

Backend создаёт проект и комнату, возвращает корректный core-summary.

### Recommended GitHub Checkpoint

```bash
git commit -m "feat: add backend prototype core"
```

---
## PHASE_4 — Rule Artifacts + Deterministic Engines / Правила и расчётные движки

**Status:** `NOT_STARTED`  

**Goal:** Подключить JSON artifacts и реализовать детерминированные движки операций, материалов, стоимости и закупки.

### Deliverables

- data/artifacts/coatings_v1.json
- data/artifacts/materials_v1.json
- data/artifacts/packages_v1.json
- data/artifacts/operations_v1.json
- data/artifacts/material_norms_v1.json
- data/artifacts/operation_material_rules_v1.json
- Execution Engine
- Material Consumption Engine
- Cost Engine
- Procurement Engine
- Validation Engine

### Acceptance Criteria

- Одинаковые входные данные дают одинаковый результат.
- Missing rule возвращает ошибку, а не пустой результат.
- Missing norm возвращает ошибку.
- package_count считается через ceil().
- loss_factor применяется.
- Тесты проверяют конкретные числовые значения.

### Exit Gate

Можно объяснить расчёт цепочкой: operation → rule → norm → formula → quantity → package_count.

### Recommended GitHub Checkpoint

```bash
git commit -m "feat: add rule artifacts and calculation engines"
```

---
## PHASE_5 — Minimal Guided Web UI / Минимальный guided web UI

**Status:** `NOT_STARTED`  

**Goal:** Сделать интерфейс, где пользователь проходит сценарий без работы с JSON.

### Deliverables

- Next.js frontend
- Projects screen
- Create Project form
- Room Setup form
- Zone and Covering Selection
- Results Dashboard
- Materials Summary
- Cost Summary
- Procurement Summary
- Errors / Warnings panel

### Acceptance Criteria

- Пользователь может пройти весь vertical slice через UI.
- Видны текущий шаг, готовые шаги и заблокированные шаги.
- Ошибки и warnings понятны.
- Результаты материалов, стоимости и закупки отображаются без JSON-консоли.
- UI достаточно responsive для мобильного браузера.

### Exit Gate

Неспециалист может создать комнату и прочитать результат.

### Recommended GitHub Checkpoint

```bash
git commit -m "feat: add minimal guided web UI"
```

---
## PHASE_6 — Prototype Integration + Release / Интеграция и выпуск Prototype v0.1

**Status:** `NOT_STARTED`  

**Goal:** Соединить backend и frontend, прогнать тесты и зафиксировать первый работающий прототип.

### Deliverables

- Working backend
- Working frontend
- Integration flow
- pytest tests
- API smoke tests
- README
- MANIFEST.json
- CHANGELOG.md
- run_report.md
- GitHub tag v0.1.0-prototype

### Acceptance Criteria

- Backend работает.
- Frontend работает.
- Core flow работает от создания проекта до закупочной ведомости.
- Тесты проходят.
- Ошибки видны пользователю.
- README объясняет запуск.

### Exit Gate

Prototype v0.1 можно показать как рабочий продуктовый срез.

### Recommended GitHub Checkpoint

```bash
git commit -m "release: prototype v0.1"
```

---
## PHASE_7 — MVP Hardening / Укрепление MVP

**Status:** `NOT_STARTED`  

**Goal:** Превратить прототип в более надёжный MVP-кандидат.

### Deliverables

- Multi-room project summaries
- Better validation messages
- More complete material rules
- Artifact validation
- Improved UI
- Basic export
- Expanded tests

### Acceptance Criteria

- Проект может содержать несколько комнат.
- Project-level summaries работают.
- Основные материалы покрыты правилами.
- Ошибки понятны.
- Расчёты проверяются тестами.

### Exit Gate

MVP можно тестировать на нескольких реалистичных сценариях ремонта.

### Recommended GitHub Checkpoint

```bash
git commit -m "feat: harden MVP candidate"
```

---
## PHASE_8 — Pilot Usage / Пилотное использование

**Status:** `NOT_STARTED`  

**Goal:** Проверить MVP на реалистичных сценариях и собрать список улучшений.

### Deliverables

- Pilot report
- Bug list
- Missing rules list
- UX friction list
- Calculation review
- Improvement backlog

### Acceptance Criteria

- Проверены минимум 5 сценариев.
- Найдены недостающие правила.
- Проверены ключевые расчёты.
- UX-проблемы зафиксированы.
- Проблемы переведены в задачи.

### Exit Gate

Понятно, что исправлять перед production-hardening.

### Recommended GitHub Checkpoint

```bash
git commit -m "docs: add pilot report"
```

---
## PHASE_9 — Production Hardening / Подготовка к production

**Status:** `NOT_STARTED`  

**Goal:** Подготовить платформу к контролируемому реальному использованию.

### Deliverables

- Authentication
- Basic RBAC
- Backup / restore
- Deployment environment
- Error logging
- Security checklist
- Database migration readiness
- Support workflow
- Bugfix policy

### Acceptance Criteria

- Приложение можно deploy.
- Данные бэкапятся.
- Restore задокументирован и протестирован.
- Доступы контролируются.
- Ошибки логируются.
- Release process понятен.

### Exit Gate

Можно выпускать production-ready v1 для ограниченного использования.

### Recommended GitHub Checkpoint

```bash
git commit -m "release: production-ready v1"
```

---
## PHASE_10 — Post-MVP Expansion / Расширение после MVP

**Status:** `FUTURE`  

**Goal:** Добавлять большие слои только после работающего ядра.

### Deliverables

- Engineering systems track
- Doors/windows/openings track
- Fixtures/furniture/appliances track
- HVAC/heating/smart-home tracks
- Suppliers/procurement ecosystem
- Contractor/customer workflows
- Mobile app
- External integrations
- Commercial subscriptions

### Acceptance Criteria

- Расширение имеет бизнес-ценность.
- Core prototype стабилен.
- Новая функция реализуется vertical slice.
- MVP не ломается.
- Есть отдельный backlog/roadmap для расширения.

### Exit Gate

Платформа растёт слоями, а не превращается в кашу.

### Recommended GitHub Checkpoint

```bash
git commit -m "docs: plan post-MVP expansion"
```

---

## 5. Current Distance to Working Prototype

```text
Current status:
- Documentation OS: mostly done
- Document cards: done
- Dependency map: done
- Lean MVP scope: in progress
- Roadmap: this document
- Backend: not started
- Frontend: not started
```

Before backend implementation, only these full specs are required:

```text
02_mvp_scope.md
05_domain_model.md
06_json_artifacts_spec.md
08_material_consumption_engine_spec.md
10_api_contract.md
26_validation_and_error_handling_spec.md
27_development_methodology_and_coding_standards.md
```

## 6. Stop Rules

```text
1. Do not add new numbered documents unless absolutely necessary.
2. Do not deepen future documents before prototype core works.
3. Do not implement production-scale features before Prototype v0.1.
4. Do not bypass MVP Scope.
5. Do not accept features without acceptance criteria.
6. Do not implement formulas without tests.
7. Do not allow silent fallback.
```

## 7. Roadmap Acceptance Criteria

This roadmap is accepted if:

```text
1. The full path from zero to production is visible.
2. Each phase has goal, deliverables, acceptance criteria and exit gate.
3. The roadmap protects the project from uncontrolled expansion.
4. The next immediate phase is clear.
5. The roadmap prioritizes a working prototype over endless documentation.
```
