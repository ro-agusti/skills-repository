# {{SKILL_NAME}}

## Descripción
[Descripción breve del propósito de este skill]

## Tipo
AI Prompt / LLM Skill

## Casos de Uso
- Caso de uso 1
- Caso de uso 2
- Caso de uso 3

## Prompt Template

### System Prompt
```
[Tu prompt de sistema aquí. Este define el comportamiento y personalidad del asistente]

Ejemplo:
Eres un experto analista de datos. Tu trabajo es analizar datasets y proporcionar
insights accionables. Siempre proporcionas ejemplos concretos y números específicos.
```

### User Prompt
```
[Template para el prompt del usuario. Usa {{variables}} para partes dinámicas]

Ejemplo:
Analiza el siguiente dataset: {{dataset}}

Enfócate en: {{focus_areas}}

Proporciona:
1. Resumen ejecutivo
2. Hallazgos clave (top {{top_n}})
3. Recomendaciones
```

## Variables

| Variable | Tipo | Descripción | Requerido | Default |
|----------|------|-------------|-----------|---------|
| `dataset` | string | Datos a analizar | ✅ | - |
| `focus_areas` | string | Áreas de enfoque | ❌ | "general" |
| `top_n` | int | Número de hallazgos | ❌ | 5 |

## Ejemplos

### Ejemplo 1: Uso Básico
```python
from scripts.compound_engine import SkillExecutor

executor = SkillExecutor('skills/ai-prompts/{{skill_name}}')
result = executor.execute(
    input_data="[datos]",
    focus_areas="ventas, tendencias",
    top_n=3
)
```

### Ejemplo 2: En una Cadena
```python
from scripts.compound_engine import SkillChain

chain = SkillChain([
    'skills/code/data-loader',
    'skills/ai-prompts/{{skill_name}}',
    'skills/code/report-generator'
])

result = chain.execute(data_source)
```

## Output Esperado

```json
{
  "summary": "Resumen del análisis...",
  "findings": [
    {
      "title": "Hallazgo 1",
      "description": "...",
      "impact": "high"
    }
  ],
  "recommendations": [...]
}
```

## Mejores Prácticas

1. **Pre-procesamiento**: Limpia los datos antes de pasarlos
2. **Context Window**: Considera el límite de tokens
3. **Iteración**: Usa múltiples llamadas para datasets grandes
4. **Validación**: Valida el output con el esquema esperado

## Dependencias

- Ninguna (skill standalone)
- O: `skills/code/data-validator`

## Testing

```bash
pytest tests/test_{{skill_name}}.py
```

## Métricas de Performance

- Latencia promedio: ~2s
- Tasa de éxito: 95%
- Token usage: ~500-1000 tokens

## Limitaciones

- Máximo 10,000 tokens de input
- Funciona mejor con datos estructurados
- Requiere contexto en español o inglés

## Changelog

### v1.0.0 - YYYY-MM-DD
- Versión inicial

## Autor
[Tu nombre]

## Licencia
MIT
