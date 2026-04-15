using SwinAdventure;

using NUnit.Framework;



namespace IdentifiableObjectTest

{

    public class IdentifiableObjectTests

    {

        private IdentifiableObject id;



        [SetUp]

        public void Setup()

        {

            id = new IdentifiableObject(new string[] { "292929292", "Viet", "Vo", "COS12345" });

        }



        [Test]

        public void TestAreYou()

        {

            Assert.That(id.AreYou("Viet"), Is.True);

        }



        [Test]

        public void TestNotAreYou()

        {

            Assert.That(id.AreYou("John"), Is.False);

        }



        [Test]

        public void TestCaseSensitive()

        {

            Assert.That(id.AreYou("viet"), Is.True);

        }



        [Test]



        public void TestFirstId()

        {

            Assert.That(id.FirstId, Is.EqualTo("292929292"));

        }



        public void TestPrivilege()

        {

            id.PrivilegeEscalation("9999");

            Assert.That(id.FirstId, Is.EqualTo("Class Tue morning"));

        }

    }

}