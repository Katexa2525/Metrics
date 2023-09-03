using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WinFormsApp_Holsted
{
  public class Metric
  {
    // конструктор
    public Metric()
    {
      FillOperators();
    }

    // поля данных
    private string buf = ""; // буфер для хранения слова (лексемы)
    private enum States { S, NUM, DLM, FIN, ID, ER, ASGN, COM, EQU } // состояния state-машины
    private States _state; // хранит текущее состояние
    private int dt = 0;

    private IList<string> Operators = new List<string>(); // список операторов
    private IList<string> KeyWords = new List<string>(); // список ключевых слов
    private IList<string> ProcAndFuncs = new List<string>(); // список функций

    // свойства
    public IList<Lexeme> Lexemes { get; set; } = new List<Lexeme>(); // список лексем разобранной программы
    public IList<TableMetric> TableMetricOperators { get; set; } = new List<TableMetric>(); // список базовых метрик для таблицы по операторам
    public IList<TableMetric> TableMetricOperands { get; set; } = new List<TableMetric>(); // список базовых метрик для таблицы по операндам
    public int DictProg { get; set; } = 0;// словарь программы
    public int LengthProg { get; set; } = 0; // длина программы 
    public double СapacityProg { get; set; } = 0; // объем программы

    public int Dict_n1 { get; set; } = 0;
    public int Dict_n2 { get; set; } = 0;
    public int Length_N1 { get; set; } = 0;
    public int Length_N2 { get; set; } = 0;
    public int Count_If { get; set; } = 0;
    public int OperLan { get; set; } = 0;


    private void FillOperators()
    {
      //Арифметические операторы Python
      Operators.Add("+"); Operators.Add("-"); Operators.Add("*"); Operators.Add("/"); Operators.Add("**");
      Operators.Add("%"); Operators.Add("//");
      //Операторы сравнения Python
      Operators.Add("=="); Operators.Add("!="); Operators.Add(">"); Operators.Add("<"); Operators.Add(">=");
      Operators.Add("<=");
      //Операторы присваивания Python
      Operators.Add("="); Operators.Add("+="); Operators.Add("-="); Operators.Add("*="); Operators.Add("/=");
      Operators.Add("%="); Operators.Add("**="); Operators.Add("//="); Operators.Add("("); Operators.Add(")");
      Operators.Add("["); Operators.Add("]");
      Operators.Add("and"); Operators.Add("break"); Operators.Add("continue"); Operators.Add("elif");
      Operators.Add("for"); Operators.Add("not"); Operators.Add("or"); Operators.Add("in"); Operators.Add("while");
      Operators.Add("try"); Operators.Add("pass"); Operators.Add("with"); Operators.Add("if");
      //Ключевые слова Python
      KeyWords.Add("import"); KeyWords.Add("def"); KeyWords.Add("else"); KeyWords.Add("except"); KeyWords.Add("return");
      // процедуры и функции языка Python
      ProcAndFuncs.Add("list"); ProcAndFuncs.Add("range"); ProcAndFuncs.Add("input"); ProcAndFuncs.Add("print"); ProcAndFuncs.Add("int");
      ProcAndFuncs.Add("set"); ProcAndFuncs.Add("str"); ProcAndFuncs.Add("len"); ProcAndFuncs.Add("max"); ProcAndFuncs.Add("dict");
      ProcAndFuncs.Add("zip"); ProcAndFuncs.Add("open"); ProcAndFuncs.Add("format"); ProcAndFuncs.Add("write"); ProcAndFuncs.Add("close");
      ProcAndFuncs.Add("upper"); ProcAndFuncs.Add("decode"); ProcAndFuncs.Add("find"); ProcAndFuncs.Add("readlines"); ProcAndFuncs.Add("urlopen");
      ProcAndFuncs.Add("append"); ProcAndFuncs.Add("count"); ProcAndFuncs.Add("lower"); ProcAndFuncs.Add("split"); ProcAndFuncs.Add("setdefault");
      ProcAndFuncs.Add("index"); ProcAndFuncs.Add("reverse"); ProcAndFuncs.Add("sum"); ProcAndFuncs.Add("next"); ProcAndFuncs.Add("choice");
      ProcAndFuncs.Add("difference"); ProcAndFuncs.Add("join"); ProcAndFuncs.Add("map"); ProcAndFuncs.Add("isdigit"); ProcAndFuncs.Add("islower");
      ProcAndFuncs.Add("isupper");
    }

    // функция поиска ключевых слов и процедур с функциями языка
    private int SearchLex(string buf, int countSpaces)
    {
      var keyWordFind = KeyWords.Count(p => p.Equals(buf)); // поиск в списке ключевых слов
      if (keyWordFind > 0)
      {
        Lexemes.Add(new Lexeme(TypeWord.Keyword, buf, countSpaces));
        return 0;
      }
      else
      {
        var procAndFuncs = ProcAndFuncs.Count(p => p.Equals(buf)); // поиск в списке процедур и функций
        if (procAndFuncs > 0)
        {
          Lexemes.Add(new Lexeme(TypeWord.ProcAndFunc, buf, countSpaces));
          return 0;
        }
        else
        {
          var operators = Operators.Count(p => p.Equals(buf));// поиск в списке операторов
          if (operators > 0)
          {
            Lexemes.Add(new Lexeme(TypeWord.Operator, buf, countSpaces));
            OperLan++;
            return 0;
          }
        }
      }
      return -1;
    }

    /// <summary> Подсчет метрик сложности по методу Холстеда  </summary>
    /// <param name="text">Текст программы</param>
    /// <returns></returns>
    public void CountMetrics(string text)
    {
      AnalysisProgram(text);

      if (Lexemes.Count() == 0)
        return;
      
      int N1_branchC = Lexemes.Count(p => p.TypeWord == TypeWord.Operator && p.Value == "("); //общее число операндов в программе по (
      int N1_branchK = Lexemes.Count(p => p.TypeWord == TypeWord.Operator && p.Value == "["); //общее число операндов в программе по [
      //словарь операторов(число уникальных операторов программы)
      int n1 = Lexemes.Where(p => (p.TypeWord == TypeWord.Operator || p.TypeWord == TypeWord.ProcAndFunc) &&
                             p.Value != "(" && p.Value != ")" && p.Value != "[" && p.Value != "]")
                      .GroupBy(x => x.Value).Select(x => x.First()).Count();
      if (N1_branchC > 0) 
        n1++; // прибавляю 1 знака скобок (
      if (N1_branchK > 0)
        n1++; // прибавляю 1 знака скобок [
      //общее число операторов в программе
      int N1 = Lexemes.Count(p => (p.TypeWord == TypeWord.Operator || p.TypeWord == TypeWord.ProcAndFunc) &&
                                   p.Value != "(" && p.Value != ")" && p.Value != "[" && p.Value != "]");
      N1 += N1_branchC + N1_branchK;

      // для таблицы расчета базовых метрик по операторам заполняю
      foreach (var item in Lexemes.Where(p => (p.TypeWord == TypeWord.Operator || p.TypeWord == TypeWord.ProcAndFunc) && p.Value != ")" && p.Value != "]")
                                  .GroupBy(x => x.Value).Select(x => x.First()))
      {
        TableMetricOperators.Add(new TableMetric 
        { 
          Oper = item.Value,
          FCount = Lexemes.Count(p => p.Value.Equals(item.Value))
        });
      }

      //словарь операндов (число уникальных операндов программы)
      int n2 = Lexemes.Where(p => p.TypeWord == TypeWord.Identifier || p.TypeWord == TypeWord.Number)
                      .GroupBy(x => x.Value).Select(x => x.First()).Count();
      //общее число операндов в программе
      int N2 = Lexemes.Count(p => p.TypeWord == TypeWord.Identifier || p.TypeWord == TypeWord.Number);

      // для таблицы расчета базовых метрик по операндам заполняю
      foreach (var item in Lexemes.Where(p => p.TypeWord == TypeWord.Identifier || p.TypeWord == TypeWord.Number)
                                  .GroupBy(x => x.Value).Select(x => x.First()))
      {
        TableMetricOperands.Add(new TableMetric
        {
          Oper = item.Value,
          FCount = Lexemes.Count(p => p.Value.Equals(item.Value))
        });
      }

      // записываю в свойства данные
      Dict_n1 = n1;
      Dict_n2 = n2;
      Length_N1 = N1;
      Length_N2 = N2;
      Count_If = Lexemes.Count(p=>p.Value.Trim().ToLower().Equals("if") || p.Value.Trim().ToLower().Equals("elif"));

      DictProg = n1 + n2;// словарь программы
      LengthProg = N1 + N2; // длина программы 
      СapacityProg = LengthProg * Math.Log(DictProg, 2);
    }

    /// <summary>Функция анализа текста программы </summary>
    /// <param name="text">Текст программы</param>
    private void AnalysisProgram(string text)
    {
      int countSpaces;
      // разделяю на строки текст из программы
      var phrases = text.Split('\n');
      // проход по массиву строк
      for (int i = 0; i < phrases.Length; i++)
      {
        if (phrases[i].Trim() == "" || phrases[i][0].ToString().Trim() == "#") // если пустая строка, или первый символ знак #, то след строка
          continue;

        countSpaces = 0;
        // определяю кол-во пробелов в начале каждой строки, чтобы потом можно было понять подчиненность операторов
        for (int j = 0; j < phrases[i].Length; j++)
        {
          if (phrases[i][j] == ' ')
            countSpaces++;
          else
            break;
        }

        // проход по строке
        for (int j = 0; j < phrases[i].Length; j++)
        {
          Analysis(phrases[i][j], phrases[i].Length, ref j, countSpaces);
        }
      }
    }

    /// <summary> Анализ символа для составления слов (лексем) программы </summary>
    /// <param name="sm">Очередной символ</param>
    /// <param name="lenStr">Длина строки phrases[i][j]</param>
    /// <param name="j">Номер j символа в строке phrases[i]</param>
    /// <param name="countSpaces">Кол-во пробелов в начале i-й строки</param>
    public void Analysis(char sm, int lenStr, ref int j, int countSpaces)
    {
      switch (_state)
      {

        case States.S: // статус очередного символа
          if (sm == ' ' || sm == '\n' || sm == '\t' || sm == '\0' || sm == '\r')
            return;
          else if (char.IsLetter(sm))
          {
            buf = "";
            buf += sm;
            _state = States.ID;
            return;
          }
          else if (char.IsDigit(sm))
          {
            dt = (int)(sm - '0');
            _state = States.NUM;
            return;
          }
          else if (sm == '#') // комментарии в конце строки
          {
            _state = States.COM;
            return;
          }
          else if (sm == '"' || sm == '\'') // строковое значение, например, "ываыва"
          {
            buf = "";
            _state = States.ASGN;
            return;
          }
          // проверяю на операции "==", ">=", "!=" и тд
          else if (sm == '=' || sm == '>' || sm == '<' || sm == '!' || sm == '+' || sm == '-' || sm == '*' || sm == '/' || sm == '%') 
          {
            buf = "";
            buf += sm;
            _state = States.EQU;
          }
          else
          {
            _state = States.DLM;
            j --;
          }
          break;
        case States.ID:
          if (char.IsLetterOrDigit(sm) || sm == '_') // определение имени идентификатора, например, Zapros или Zapros_1qwe
          {
            buf += sm;
          }
          else
          {
            if (SearchLex(buf, countSpaces) == -1)
            {
              // Проверяю, какая предыдущая лексема в списке, если def, то к TypeWord.ProcAndFunc, иначе TypeWord.Identifier
              if (Lexemes.Count() > 0 && Lexemes[Lexemes.Count() - 1].Value == "def")
                Lexemes.Add(new Lexeme(TypeWord.ProcAndFunc, buf, countSpaces));
              else
                Lexemes.Add(new Lexeme(TypeWord.Identifier, buf, countSpaces));
            }
            _state = States.S;
            j --; // проверяю, что в переменной sm, если, например, ( , то уменьшаю индекс для phrases[i][j]
          }
          break;
        case States.NUM:
          if (char.IsDigit(sm))
          {
            dt = dt * 10 + (int)(sm - '0');
          }
          else
          {
            buf = dt.ToString();
            Lexemes.Add(new Lexeme(TypeWord.Number, buf, countSpaces));
            _state = States.S;
            j--;
          }
          break;
        case States.DLM:
          buf = "";
          buf += sm;
          if (SearchLex(buf, countSpaces) == -1)
          {
            Lexemes.Add(new Lexeme(TypeWord.Separator, buf, countSpaces));
            _state = States.S;
          }
          else
            _state = States.S;
          break;
        case States.COM:
          buf = "";
          j = lenStr;
          _state = States.S;
          break;
        case States.ASGN:
          if (sm != '"' && sm != '\'')
          {
            buf += sm;
          }
          else
          {
            Lexemes.Add(new Lexeme(TypeWord.String, buf, countSpaces));
            _state = States.S;
          }
          break;
        case States.EQU: // проверка для знака '='
          if (sm.ToString() == buf) // ловлю оператор типа **= или //=
            buf += sm;
          else if (sm != '=') 
          {
            if (SearchLex(buf, countSpaces) == -1)
            {
              Lexemes.Add(new Lexeme(TypeWord.Separator, buf, countSpaces));
            }
            j--;
            _state = States.S;
          }
          else
            buf += sm;
          break;
        case States.ER:
          //MessageBox.Show("Ошибка в программе");
          _state = States.FIN;
          break;
        case States.FIN:
          //MessageBox.Show("Лексический анализ закончен");
          break;
      }
    }

    /// <summary> Метод для нахождения и возврата максимальной вложенности оператора If </summary>
    /// <returns></returns>
    public int MaxDepthCLI()
    { 
      int maxDepth = 0;
      int countSpaces = 0;
      int curDepth = 0;
      for (int i = 0; i < Lexemes.Count; i++)
      {
        
        if (Lexemes[i].Value == "if" || Lexemes[i].Value == "elif")
        {
          int j = i + 1;
          countSpaces = Lexemes[i].СountSpaces; // кол-во отступов в строке с if
          curDepth = 1; // текущая начальная вложенность
          // ищу лексему двоеточие в конце if
          while (Lexemes[j].СountSpaces == countSpaces && Lexemes[j].Value != ":")
          {
            i = ++j;
          }
          i = ++j;
          // ищу вложенные if
          while (Lexemes[j].СountSpaces > countSpaces) // проверка подчиненных лексем
          {
            if (Lexemes[j].Value == "if" || Lexemes[j].Value == "elif")
              curDepth++;
            j++;
          }
          i = j;
          maxDepth = curDepth > maxDepth ? curDepth : maxDepth;
          
        }
      }
      return maxDepth;
    }
  }
}
