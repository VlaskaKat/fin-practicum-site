// Вставить в Google-таблицу: Расширения → Apps Script. Принимает заявки с сайта.
function doPost(e) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
  var head = ['Дата и время', 'Имя', 'Email', 'Телефон', 'Ник в Telegram', 'Тариф', 'Статус', 'Комментарий'];
  if (sheet.getRange(1, 1, 1, head.length).getValues()[0].join('|') !== head.join('|')) {
    sheet.getRange(1, 1, 1, head.length).setValues([head]).setFontWeight('bold');
    sheet.setFrozenRows(1);
  }
  var d = JSON.parse(e.postData.contents || '{}');
  var clean = function (x) { x = String(x || '').slice(0, 300); return /^[=+\-@]/.test(x) ? "'" + x : x; };
  sheet.appendRow([new Date(), clean(d.name), clean(d.email), clean(d.phone), clean(d.telegram), clean(d.plan), 'Новая', '']);
  return ContentService.createTextOutput('ok');
}
