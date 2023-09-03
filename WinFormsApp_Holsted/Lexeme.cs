namespace WinFormsApp_Holsted
{
  /// <summary> Класс для идентификации лексемы </summary>
  public class Lexeme
  {
    public TypeWord TypeWord { get; set; }
    public string Value { get; set; }
    public int СountSpaces { get; set; } // кол-во пробелов в строке кода, где состоит лексема

    public Lexeme(TypeWord typeWord, string value, int countSpaces)
    {
      this.TypeWord = typeWord;
      this.Value = value;
      this.СountSpaces = countSpaces;
    }
  }
}
