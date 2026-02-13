# {{SKILL_NAME}}

## Descripción
[Descripción breve del propósito de este skill]

## Tipo
Code Skill / Python Module

## Instalación

```bash
# Si tiene dependencias específicas
pip install -r requirements.txt
```

## Uso Rápido

```python
from skills.code.{{skill_name}}.{{module_name}} import execute

result = execute(
    input="datos de entrada",
    param1="valor1",
    param2="valor2"
)
```

## API Reference

### Función Principal: `execute()`

```python
def execute(input: Any, **kwargs) -> Any:
    """
    Ejecuta la funcionalidad principal del skill
    
    Args:
        input: Datos de entrada principal
        **kwargs: Parámetros adicionales
        
    Returns:
        Resultado procesado
        
    Raises:
        ValueError: Si los parámetros son inválidos
        RuntimeError: Si hay error en procesamiento
    """
```

### Clase Principal: `{{ClassName}}`

```python
class {{ClassName}}:
    """Clase principal del skill"""
    
    def __init__(self, config: dict = None):
        """
        Inicializa el skill
        
        Args:
            config: Configuración opcional
        """
        
    def run(self, data: Any) -> Any:
        """
        Ejecuta el procesamiento
        
        Args:
            data: Datos a procesar
            
        Returns:
            Resultado
        """
```

## Parámetros

| Parámetro | Tipo | Descripción | Default |
|-----------|------|-------------|---------|
| `input` | Any | Datos de entrada | - |
| `param1` | str | Descripción param1 | "default" |
| `param2` | int | Descripción param2 | 10 |

## Ejemplos

### Ejemplo 1: Uso Básico

```python
from skills.code.{{skill_name}} import execute

data = "ejemplo de datos"
result = execute(input=data)
print(result)
```

**Output:**
```
Resultado esperado...
```

### Ejemplo 2: Con Configuración

```python
from skills.code.{{skill_name}}.{{module_name}} import {{ClassName}}

processor = {{ClassName}}(config={
    'option1': True,
    'option2': 'value'
})

result = processor.run(data)
```

### Ejemplo 3: En Pipeline

```python
from scripts.compound_engine import SkillChain

chain = SkillChain([
    'skills/code/{{skill_name}}',
    'skills/ai-prompts/analyzer',
])

result = chain.execute(input_data)
```

## Testing

### Ejecutar Tests

```bash
# Todos los tests
pytest skills/code/{{skill_name}}/tests/

# Tests específicos
pytest skills/code/{{skill_name}}/tests/test_{{module_name}}.py

# Con cobertura
pytest --cov=skills/code/{{skill_name}} tests/
```

### Estructura de Tests

```python
import pytest
from {{module_name}} import execute, {{ClassName}}

class Test{{ClassName}}:
    def test_basic_functionality(self):
        result = execute(input="test")
        assert result is not None
        
    def test_with_parameters(self):
        result = execute(input="test", param1="custom")
        assert "custom" in str(result)
        
    @pytest.mark.parametrize("input_val,expected", [
        ("input1", "output1"),
        ("input2", "output2"),
    ])
    def test_multiple_cases(self, input_val, expected):
        result = execute(input=input_val)
        assert result == expected
```

## Performance

- **Complejidad temporal**: O(n)
- **Complejidad espacial**: O(1)
- **Throughput**: ~1000 items/sec
- **Latencia promedio**: <10ms

## Dependencias

```python
# requirements.txt
numpy>=1.24.0
pandas>=2.0.0
# etc.
```

## Integración

### Con otros Skills

```python
# Ejemplo de integración
from skills.code.{{skill_name}} import execute as skill_execute
from skills.code.other_skill import execute as other_execute

result1 = skill_execute(data)
result2 = other_execute(result1)
```

### En API

```python
from fastapi import FastAPI
from skills.code.{{skill_name}} import execute

app = FastAPI()

@app.post("/process")
async def process(data: dict):
    result = execute(input=data)
    return {"result": result}
```

## Troubleshooting

### Error Común 1
**Problema**: [Descripción]
**Solución**: [Solución]

### Error Común 2
**Problema**: [Descripción]
**Solución**: [Solución]

## Mejores Prácticas

1. **Validación de Input**: Siempre valida los datos de entrada
2. **Error Handling**: Usa try-except apropiadamente
3. **Logging**: Usa logging para debugging
4. **Type Hints**: Usa anotaciones de tipo

## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Optimización de performance

## Contributing

Ver [CONTRIBUTING.md](../../../CONTRIBUTING.md)

## Changelog

### v1.0.0 - YYYY-MM-DD
- Versión inicial

### v1.1.0 - YYYY-MM-DD
- Feature nueva
- Bug fix

## Licencia

MIT

## Autor

[Tu nombre]

## Referencias

- [Documentación relacionada]
- [Papers o recursos]
