class Formatters:
  @staticmethod
  def usd(value):
    if not len(value):
      return ""
    if "." in value:
      return ".".join([value.split(".")[0], value.split(".")[1][:2]])
    else:
      cln = value.replace(",", "")
      return f"{int(cln):,}"

  @staticmethod
  def usdToFloat(usd):
    return float(usd.replace(",", ""))

  @staticmethod
  def floatToUsd(usd):
    return f"{usd:,.2f}"