r301 %r{.*}, 'http://docs-hdb-staging$&', if: Proc.new {|rack_env|
  rack_env['SERVER_NAME'] == 'docs-hawq-staging'
}
rewrite '/', '/20/overview/HAWQOverview.html'
r301 '/index.html', '/20/overview/HAWQOverview.html'

