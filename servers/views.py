from django.http import HttpResponse
from .singleton import TestDataManager
from .models import DataGeneratorFactory
def index(request):
    html = """
    <h1>Система управления тестовыми данными</h1>
    <ul>
        <li><a href="/servers/generate/">Сгенерировать данные (Factory + Singleton)</a></li>
        <li><a href="/servers/datasets/">Показать все наборы (Singleton)</a></li>
    </ul>
    """
    return HttpResponse(html)
def generate(request):
    try:
        manager = TestDataManager()
        results = []
        for data_type, count in [("users", 3), ("orders", 2), ("products", 4)]:
            generator = DataGeneratorFactory.create(data_type, count)
            items = generator.generate()
            manager.add_dataset(data_type, items)
            results.append(generator.get_info())
            results.append(f"  → {items}")
        html = "<h2>Сгенерировано через Factory:</h2><pre>"
        html += "\n".join(results)
        html += "</pre><p>Данные сохранены в Singleton TestDataManager.</p>"
        html += '<p><a href="/servers/datasets/">Посмотреть все наборы</a></p>'
        return HttpResponse(html)
    except ValueError as e:
        return HttpResponse(f"Ошибка Factory: {e}", status=400)
def datasets(request):
    manager = TestDataManager()
    all_data = manager.get_all_datasets()
    manager2 = TestDataManager()
    same = id(manager) == id(manager2)
    html = "<h2>Все наборы данных (Singleton)</h2>"
    html += f"<p><b>id(manager1) == id(manager2):</b> {same}</p>"
    html += f"<p><b>manager1 is manager2:</b> {manager is manager2}</p>"
    if not all_data:
        html += "<p>Данных пока нет. <a href='/servers/generate/'>Сгенерировать</a></p>"
    else:
        html += "<ul>"
        for data_type, items in all_data.items():
            html += f"<li><b>{data_type}</b>: {items}</li>"
        html += "</ul>"
    return HttpResponse(html)