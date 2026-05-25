# Pattern Example Template

Copy this folder when adding a **new** pattern or a second example for an existing one.

```bash
cp -r templates/pattern-example patterns/XX-your-pattern-name
# Rename XX-your-pattern-name and update README.md
```

## Folder layout

```
XX-your-pattern-name/
├── README.md       # Pattern overview (from docs or your research)
├── use-case.md     # Real-life problem — fill in completely
└── example/
    ├── README.md   # How to run
    ├── main.py     # Entry point
    └── ...         # Pattern-specific modules
```

## Checklist before marking done

- [ ] `use-case.md` describes a concrete real-world scenario
- [ ] `example/` runs with documented prerequisites
- [ ] Pattern README links to your example
- [ ] Shared code lives in `shared/` if reused across patterns
- [ ] No secrets committed — use `.env` from `.env.example`

## README template (pattern root)

```markdown
# Pattern Name

## What it is
...

## When to use it
...

## When not to use it
...

## Related patterns
- [Other](../XX-other/)

## Example
See [`example/`](example/).

## Real-life use case
See [`use-case.md`](use-case.md).
```

## use-case.md template

See [`use-case.md`](use-case.md) in this folder.
