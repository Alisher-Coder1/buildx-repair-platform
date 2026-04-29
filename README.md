# Buildx Repair Platform

## Статус проекта

- Project: Buildx Repair Platform
- Current Phase: Phase 1 — Documentation Architecture
- Implementation Status: Код платформы пока не пишется
- Documentation Status: Documentation Operating System v0.1.1 initialized
- Date: 2026-04-29

## Главная цель

Создать управляемую, индексированную, проверяемую документационную систему для будущей разработки платформы ремонта.

Платформа в будущем должна отвечать на главный пользовательский вопрос:

> Что делать, в каком порядке делать, сколько материала уйдёт, сколько это будет стоить и что нужно купить.

## Текущий этап

Phase 1 не реализует backend, frontend, API или расчётные движки.

Phase 1 создаёт основу:

- структуру проекта;
- индекс документации;
- реестр документации;
- шаблон документа;
- audit matrix;
- dependency map;
- governance-подход;
- backlog для open questions, future scope и change requests;
- правила подготовки документов к audit/freeze.

## Стартовая структура

```text
buildx-repair-platform/
├── README.md
├── MANIFEST.json
├── CHANGELOG.md
├── run_report.md
├── docs/
│   ├── 00_documentation_index.md
│   ├── 13_document_acceptance_and_governance.md
│   ├── 45_documentation_writing_methodology_and_style_guide.md
│   ├── documentation_registry_v0.1.yaml
│   ├── audit/
│   │   ├── documentation_audit_question_matrix_v0.1.md
│   │   └── documentation_dependency_map_v0.1.md
│   └── templates/
│       └── document_template.md
├── data/
│   └── artifacts/
└── backlog/
    ├── open_questions.md
    ├── change_requests.md
    └── future_scope.md
```

## Принцип работы

Документация должна быть подготовлена так, чтобы разработчик, команда или AI coding agent могли реализовать платформу без устных догадок.

Основной подход:

```text
documentation-first
specification-complete
domain-first
rule-driven
test-first
no silent fallback
```

## GitHub checkpoint policy

После каждого завершённого этапа:

1. обновить документацию;
2. обновить `CHANGELOG.md`;
3. обновить `MANIFEST.json`;
4. обновить `run_report.md`;
5. сделать commit;
6. выполнить push в GitHub;
7. при milestone — создать tag/release.


## Dependency map

The file below is now part of the Phase 1 documentation operating system:

```text
docs/audit/documentation_dependency_map_v0.1.md
```

It is the human-readable map of document dependencies, update-together rules and AI reading packs.

Before approving or freezing documents, use it together with:

```text
docs/documentation_registry_v0.1.yaml
docs/audit/documentation_audit_question_matrix_v0.1.md
```
