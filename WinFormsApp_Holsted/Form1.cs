using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Windows.Forms;

namespace WinFormsApp_Holsted
{
  public partial class Form1 : Form
  {
    private Metric metric;
    public Form1()
    {
      InitializeComponent();
      metric = new Metric();
      openFileDialog1.Filter = "Python files(*.py)|*.py|All files(*.*)|*.*";
    }

    private void button_close_Click(object sender, EventArgs e)
    {
      Close();
    }

    private void button_openFile_Click(object sender, EventArgs e)
    {
      if (openFileDialog1.ShowDialog() == DialogResult.Cancel)
        return;
      // получаем выбранный файл
      string filename = openFileDialog1.FileName;
      // читаем файл в строку
      string fileText = System.IO.File.ReadAllText(filename);
      textBox_Filename.Text = filename;

      // считаем метрики файла
      metric.CountMetrics(fileText);

      // вывожу лексический разбор в ListView
      int num = 1;
      dataGridView_lex.Rows.Clear();
      foreach (var item in metric.Lexemes)
      {
        dataGridView_lex.Rows.Add(num, Convert.ToString(item.TypeWord), item.СountSpaces, item.Value);
        num++;
      }
      //
      num = 1;
      dataGridView_Opr.Rows.Clear();
      foreach (var item in metric.TableMetricOperators)
      {
        dataGridView_Opr.Rows.Add(num, item.Oper, item.FCount);
        num++;
      }
      //
      num = 1;
      dataGridView_Oprd.Rows.Clear();
      int SumSpen = 0;
      int chepP = 0;
      int chepM = 0;
      int chepT = 0;
      int chepC = 0;

      int chepMV = 0;
      int chepCV = 0;
      int chepTV = 0;
      int chepPV = 0;
      dataGridView_Chepin.Rows.Clear();
      foreach (var item in metric.TableMetricOperands)
      {
        dataGridView_Oprd.Rows.Add(num, item.Oper, item.FCount,
                                  (int.TryParse(item.Oper, out int result) ? 0 : item.FCount - 1)); // спен
        SumSpen += (int.TryParse(item.Oper, out int result1) ? 0 : item.FCount - 1);
        num++;
        if (!int.TryParse(item.Oper, out int result2) && !bool.TryParse(item.Oper, out bool result3))
        {
          // поиск названия переменных в списке лексем
          for (int i = 0; i < metric.Lexemes.Count; i++)
          {
            if (metric.Lexemes[i].Value.Trim().Equals(item.Oper.Trim())) //если нашли переменную
            {
              if (FindOperChepС(i, item.Oper, metric.Lexemes) == true)
              {
                chepC++;
                dataGridView_Chepin.Rows.Add(item.Oper, "C");
                if (FindOperChepVvod(i, item.Oper, metric.Lexemes) == true)
                {
                  dataGridView_ChepinVvod.Rows.Add(item.Oper, "C");
                  chepCV++;
                }
                break;
              }
              else if (FindOperChepM(i, item.Oper, metric.Lexemes) && metric.Lexemes.Count(p => p.Value.Trim().Equals(item.Oper.Trim())) > 1)
              {
                chepM++;
                dataGridView_Chepin.Rows.Add(item.Oper, "M");
                if (FindOperChepVvod(i, item.Oper, metric.Lexemes))
                {
                  dataGridView_ChepinVvod.Rows.Add(item.Oper, "M");
                  chepMV++;
                }
                break;
              }
              else if (metric.Lexemes.Count(p => p.Value.Trim().Equals(item.Oper.Trim())) == 1)
              {
                chepT++;
                dataGridView_Chepin.Rows.Add(item.Oper, "T");
                if (FindOperChepTVvod(i, item.Oper, metric.Lexemes))
                {
                  dataGridView_ChepinVvod.Rows.Add(item.Oper, "T");
                  chepTV++;
                }
                break;
              }
              else
              {
                chepP++;
                dataGridView_Chepin.Rows.Add(item.Oper, "P");
                if (FindOperChepVvod(i, item.Oper, metric.Lexemes))
                {
                  dataGridView_ChepinVvod.Rows.Add(item.Oper, "P");
                  chepPV++;
                }
                break;
              }
            }
          }
        }
      }
      // заполняю поля
      textBox_n1.Text = metric.Dict_n1.ToString();
      textBox_n2.Text = metric.Dict_n2.ToString();
      textBox_N_1.Text = metric.Length_N1.ToString();
      textBox_N_2.Text = metric.Length_N2.ToString();
      textBox_dictProg.Text = metric.DictProg.ToString();
      textBox_lenProg.Text = metric.LengthProg.ToString();
      textBox_VProg.Text = Math.Round(metric.СapacityProg, 2).ToString();
      //Для Джилба
      textBox_CL.Text = metric.Count_If.ToString();
      textBox_cloper.Text = (Math.Round((double)metric.Count_If / (double)metric.OperLan, 2)).ToString();
      textBox_CLI.Text = (metric.MaxDepthCLI() - 1).ToString();
      //Метрики потока данных
      textBox_Spen.Text = SumSpen.ToString();
      textBox_P.Text = chepP.ToString();
      textBox_C.Text = chepC.ToString();
      textBox_T.Text = chepT.ToString();
      textBox_M.Text = chepM.ToString();
      textBox_Q.Text = (chepP + 2 * chepM + 3 * chepC + 0.5 * chepT).ToString();

      textBox_MV.Text = chepMV.ToString();
      textBox_CV.Text = chepCV.ToString();
      textBox_TV.Text = chepTV.ToString();
      textBox_PV.Text = chepPV.ToString();
      textBox_QV.Text = (chepPV + 2 * chepMV + 3 * chepCV + 0.5 * chepTV).ToString();
    }

    private bool FindOperChepM(int k, string oper, IList<Lexeme> Lexemes)
    {
      for (int i = k; i < Lexemes.Count; i++)
      {
        if (Lexemes[i].Value.Trim().Equals(oper.Trim()))
        {
          if (i + 1 >= Lexemes.Count)
            break;
          string ss = Lexemes[i + 1].Value.Trim().ToLower();
          if (ss == "="||ss == "-=" || ss == "+=" || ss == "/=" || ss == "*=" || ss == "//=" || ss == "**=" || ss == "%=")
          {
            return true;
          }

        }
      }
      return false;
    }

    private bool FindOperChepVvod(int k, string oper, IList<Lexeme> Lexemes)
    {
      for (int i = k; i < Lexemes.Count; i++)
      {
        if (Lexemes[i].Value.Trim().Equals(oper.Trim()))
        {
          if (i + 2 >= Lexemes.Count) { }
          else
          {
            string ss1 = Lexemes[i + 2].Value.Trim().ToLower();
            if (ss1 == "input")
            {
              return true;
            }
          }
          if (i - 2 < 0) { }
          else
          {
            string ss2 = Lexemes[i - 2].Value.Trim().ToLower();
            if (ss2 == "print")
            {
              return true;
            }
          }
        }
      }
      return false;
    }

    private bool FindOperChepTVvod(int k, string oper, IList<Lexeme> Lexemes)
    {
      for (int i = k; i < Lexemes.Count; i++)
      {
        if (Lexemes[i].Value.Trim().Equals(oper.Trim()))
        {
          if (i + 2 >= Lexemes.Count) {
            break;
          }
          else
          {
            string ss1 = Lexemes[i + 2].Value.Trim().ToLower();
            if (ss1 == "input")
            {
              return true;
            }
          }
        }
      }
      return false;
    }

    private bool FindOperChepС(int k, string oper, IList<Lexeme> Lexemes)
    {
      for (int i = k; i < Lexemes.Count; i++)
      {
        if (Lexemes[i].Value.Trim().Equals(oper.Trim()))
        {
          if (i - 1 < 0)
            break;
          else
          {
            string ss = Lexemes[i - 1].Value.Trim().ToLower();
            if (ss == "while" || ss == "for" || ss == "if" || ss == "in" || ss == "elif")
            {
              return true;
            }
          }
        }
      }
      return false;
    }
    private void button_saveF_Click(object sender, EventArgs e)
    {
      if (metric.Lexemes.Count == 0)
      {
        MessageBox.Show("Коллекция лексем пуста!");
        return;
      }
      int num = 1;
      using (StreamWriter writer = File.CreateText("Lexemes.txt"))
      {
        foreach (var item in metric.Lexemes)
        {
          string str = num.ToString() + " | " + Convert.ToString(item.TypeWord) + " | " + item.Value;
          writer.WriteLine(str);
          num++;
        }
        MessageBox.Show("Коллекция записана в файл!");
      }
    }
  }
}
